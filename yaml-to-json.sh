# Run with:
# bash yaml-to-json.sh < some-yaml.yaml
# to see JSON

python -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout)'
