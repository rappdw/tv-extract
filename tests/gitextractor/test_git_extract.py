from tv_extract.gitextractor.extract_revision_graph import command_dict, get_revision_from_line, _extract_revision_graph


def test_get_rev_from_line():
    line = 'tree_hash|sha|timestamp|date time tz_offset|author|email@domain||comments'
    revision, parents = get_revision_from_line(line)
    assert revision
    assert parents
    assert len(parents) == 1
    assert not parents[0]
    assert revision.hash == 'sha'
    assert revision.stamp == 0
    assert revision.author == 'author'
    assert revision.email == 'email@domain'
    assert revision.domain == 'domain'
    assert revision.comments == 'comments'
    assert revision.timezone == 'tz_offset'

def get_output(cmds):
    for k, v in command_dict.items():
        if v == cmds:
            if k == 'original_commit':
                return 'sha:1'
            elif k == 'initial_revisions':
                return '''
tree:1|sha:1|1|2018-07-18 11:11:28 -0600|author1|author1@domain||commit #0               
tree:2|sha:2|2|2018-07-18 11:11:28 -0600|author1|author1@domain|sha:1|commit #1               
tree:3|sha:3|3|2018-07-18 11:11:28 -0600|author2|author2@domain|sha:1 sha:2|commit #3               
                '''
            elif k == 'master_revisions':
                return '''
tree:1|sha:1|1|2018-07-18 11:11:28 -0600|author1|author1@domain||commit #0               
tree:3|sha:3|3|2018-07-18 11:11:28 -0600|author2|author2@domain|sha:1 sha:2|commit #3               
                '''
    return ''

def get_test_graph():
    return _extract_revision_graph(get_output)

def test_extract_revisions():
    graph = get_test_graph()
    assert graph
    assert len(graph.revisions) == 3
    assert len(graph.not_a_merge) == 2
    assert len(graph.merges) == 1
    assert 'sha:1' in graph.not_a_merge
    assert 'sha:2' in graph.not_a_merge
    assert 'sha:3' in graph.merges
    assert 'sha:1' in graph.master_revs
    assert 'sha:3' in graph.master_revs
