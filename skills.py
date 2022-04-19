t1 = """**Python** - *I write more code than emails.* As of today, it replaced calculator, Excel, Notepad+. Mostly used libraries: `netmiko`, `napalm`, `requests`, `click `, `pandas`, `rich`, `pydantic` 
**PyCharm** - Still discovering why I want Premium. My main window(s) 
**PowerShell, Bash** - In use. For now, googling skill was enough to get the desire results.
**Network**  - I know . I can move around and find myself in it. Never implemented any routing. I understand almost everything in network talking. Close to CCNA. 
**Azure Devops** - Countless Repos, many Pipelines, single Artifact. 
**Windows** - I can find or/and set whatever is required, for currently used Windows version on my workstation.
**RHEL, *ubuntu** - Basic administrator level. """


t11 = """<ul>
<strong>Python</strong> - I write more code than emails. As of today, it replaced calculator, Excel, Notepad+. Mostly used libraries: `netmiko`, `napalm`, `requests`, `click `, `pandas`, `rich`, `pydantic`
<strong>PyCharm</strong> - Still discovering why I want Premium. My main window(s)
<strong>PowerShell, Bash</strong> - In use. For now, googling skill was enough to get the desire results.
<strong>Network</strong> - I know . I can move around and find myself in it. Never implemented any routing. I understand almost everything in network talking. Close to CCNA.
<strong>Azure Devops</strong> - Countless Repos, many Pipelines, single Artifact.
<strong>Windows</strong> - I can find or/and set whatever is required, for currently used Windows version on my workstation.
<strong>RHEL, ubuntu</strong> - Basic administrator level.
</ul>"""

t2 = """ - Problem finder and solver.
English - Yes, we can."""

t3 = """I write more code than emails, usually in **Python** using **PyCharm**. In particular use case, I'm using **PowerShell** or **Bash**. 

My **Network Knowledge** is close to CCNA but without routing part. Nevertheless, I'm quite familliar with device such as: **Palo Alto**, **Ciscio IOS/NX/ISE** and **many others**."""
t = t1


def cleanse(s: str):
    chars = ['*']
    new_s = s
    for c in chars:
        new_s = new_s.replace(c, "")

    pre, suf = new_s.split("-", maxsplit=1)
    bold_pre = f"<strong>{pre.strip()}</strong>"
    bold_str = " - ".join([bold_pre,suf.strip()])
    return bold_str


tl = t.splitlines()

clean = []

startstr = """<ul>"""
intmp = lambda x: f"<li> {x}</li>"
endstr = """</ul>"""

clean.append(startstr)
for l in tl:
    clean.append(intmp(cleanse(l)))

clean.append(endstr)
print(clean)

print(f"ggg\n\n\n")

for cln in clean:
    print(f"{cln}")
