# Get Target Issues

Creates a JSON file in current directory containing all issues as well as an issues count from your specified target.

## REQUIRED:

--org - Input your org name i.e. "Org example"

--target - Input your target name i.e. "joeshope/get_target_issues" (May be set using --target-reference="Example" when using the Snyk CLI: https://docs.snyk.io/snyk-cli/commands/monitor#target-reference-less-than-target_reference-greater-than)

--token - Input your Snyk API token (You can find it here: https://docs.snyk.io/snyk-api/authentication-for-api)

## How to use:
- Clone repo
- Navigate into directory
- Run using the below argument

example: <pre><code>python3 main.py --org "Org Example" --target "target/example" --token {token} </code></pre>

You will append a saved file locally "results.json" that can be reviewed. *NOTE* When ran multiple times, this will keep appending the same json
