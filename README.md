# Jane the Ripper — Simple Password Cracker

Place `hashes.txt` and `wordlist.txt` in the same folder as the script.

## Use

Jane The Ripper is a parody script of John the Ripper. I Promsise its much less effecient but I made it so it's cooler. It is used to brute force hashes and get the plain text

## Scripts

* `simple_md5_cracker.py` — easy nested-loop MD5 cracker.
* `multi_algo_easy_cracker.py` — same easy approach but supports `md5`, `sha1`, or `sha256`. It asks which algorithm to use.

## Run

```bash
python jane.py
```

