
config_json = '''
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