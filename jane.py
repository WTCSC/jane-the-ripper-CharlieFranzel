import hashlib

algo = input("algorithm (md5/sha1/sha256): ").strip().lower()   # Gets the algorithm from user
if algo not in ("md5","sha1","sha256"):
    print("unsupported")     # If unsupported algorithm, exit
    raise SystemExit

hashes = [h.strip().lower() for h in open("hashes.txt")]  # Reads target hashes from file
words = [w.strip() for w in open("wordlist.txt")] # Reads wordlist from file

print("\nCracking!!!")
for w in words:
    h = hashlib.new(algo, w.encode()).hexdigest() # Hashes the word using the selected algorithm
    for target in hashes:
        if h == target:
            print(f"[+] Cracked: {target}  > {w}") # If a match is found, print the cracked hash and word
print("--- CRACKING FINISHED ---")
