import sys
import requests
import hashlib

#this function will take the first five characters of the hashed password and return the response from the api
def api_fetch(first_five_char):
    url= "https://api.pwnedpasswords.com/range/" + first_five_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again")
    return res
    
#this function will take the response from the api and the tail of the hashed password and return the count of the password leaks
def get_password_leaks_count(hashes,tail):
    for line in hashes.text.splitlines():
        hash, count = line.split(":")
        if hash == tail:
            return count
    return 0
        

#this function will take the password and return the count of the password leaks
def get_hashed_password(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_five_char, tail = sha1password[:5], sha1password[5:]
    count = get_password_leaks_count(api_fetch(first_five_char),tail)
    return count


#this function will take the password and return the count of the password leaks
if __name__ == "__main__":
    passwords = sys.argv[1:]
    for password in passwords:
        count = get_hashed_password(password)
        if count:
            print(f"{count} times found, you should change your password")
        else:
            print("Your password is safe")
    


  



   
  





        