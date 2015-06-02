import re
import sys

regex = re.compile(": (.+)")
completeString = ""
with open(sys.argv[1]) as f:
  for line in f:
    if "de:" in line:
      line = line.replace("de:", "translations =")
    if "en:" in line:
      line = line.replace("en:", "translations =")

    result = regex.search(line)

    if result:
      if not "\"" in result.group(1)[:1]:
        if not "\'" in result.group(1)[:1]:
          line = line.replace(result.group(0), ": \"" + result.group(1) + "\"");
    completeString += line
  completeString += "`export default translations`"

  f = open(sys.argv[1] + ".coffee","w")
  f.write(completeString)
  f.close()
