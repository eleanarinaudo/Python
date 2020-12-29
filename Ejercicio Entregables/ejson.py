import json
usuarios = json.loads(input())
email = input()
password = input()

{
    "usuarios": ["mica@mail.co", "jerry@gma.com","alber@soup.co"],
    "contra": ["abc123","caballitos","yoloswag"]
}

exists=False
OK=False
for i,u in enumerate(usuarios["usuarios"]):
    if email==u:
        exists=True
        if password == usuarios["contra"][i]:
            OK=True

if OK:
    print("OK")
elif exists:
    print("NO")
else:
    print("DNE")
    
