# Get Project Issues

Creates a JSON file in current directory containing issues from your specified project.

## REQUIRED:

--org - Input your org name i.e. "Org example"
--project - Input your project name i.e. "Project Example"
--token - Input your Snyk API token (You can find it here: https://docs.snyk.io/snyk-api/authentication-for-api)

How to use:
- Clone repo
- Navigate into directory
- Run using the below argument

example: <pre><code>python3 main.py --org="Org Example" --project="Project Example" --token=<token> </code></pre>

You will have a saved file locally "results.json" that can be reviewed.
