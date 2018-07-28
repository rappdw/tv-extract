from typing import List

from tv_extract.data.pr import PullRequest
from tv_extract.data.extract import Extract
from tv_extract.gitextractor.extract_revision_graph import command_dict, get_revision_from_line, _extract_revision_graph
from tv_extract.gitextractor.extract_pr_data import extract_pr_data
from tv_extract.git_extract import GitExtractor

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

def test_extract_pr():
    graph = get_test_graph()
    prs: List[PullRequest] = []
    extract_pr_data(lambda pr: prs.append(pr), graph)
    assert len(prs) == 1
    assert prs[0].stamp == 3

class Verifier:
    def __init__(self):
        self.accumulator = []

    def writerow(self, row: List[str]):
        self.accumulator.append(row)

class ExtractionVerifier:
    def __init__(self):
        self.author_totals_info_writer = Verifier()
        self.revision_info_writer = Verifier()
        self.loc_info_writer = Verifier()
        self.loc_delta_writer = Verifier()
        self.repo_info_writer = Verifier()
        self.prs_info_writer = Verifier()

def test_gitextractor():
    graph = get_test_graph()
    extractor = GitExtractor(Extract("test", []), '', None)
    extractor.files = ExtractionVerifier()
    extractor.process_graph(None, graph)
    print(extractor.files)