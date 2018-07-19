import json
from tv_extract.util.cli import extract_config_from_json

test_config_json = '''
{
  "extracts": [
    {
      "name": "test",
      "repos": [
        {
          "name": "TeamViewer",
          "remote": "git@github.com:rappdw/TeamViewer.gitextractor"
        },
        {
          "name": "team-viewer-extract",
          "remote": "git@github.com:rappdw/team-viewer-extract.gitextractor"
        }
      ],
      "start_date": "2018-07-18"
    }
  ],
  "output_path": "~/.local/share/cache/TeamViewer",
  "mailmap_file": "~/.local/share/cache/.mailmap",
  "logging": 20
}'''


def test_config_extractions():
    config = extract_config_from_json(json.loads(test_config_json))
    assert len(config.extracts) == 1
    assert config.extracts[0].name == 'test'
    assert len(config.extracts[0].repos) == 2
    assert config.output_path == "~/.local/share/cache/TeamViewer"