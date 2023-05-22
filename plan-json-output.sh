export outjson=$(python3 plan_json-output.py)
rich --json $(echo $outjson)
echo $outjson > test.json

echo $(cat test.json) | jq -r .keys
echo $(cat test.json) | jq -r jq -r '.resource_changes[].address'
echo $(cat test.json) | jq 'map(select(.resource_changes.change.actions[] != "no-op"))'