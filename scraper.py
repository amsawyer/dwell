from flask import Flask, jsonify, render_template, request
import requests
import string

def main():
    city_start = idx_start = 0
    page = requests.get('http://www.infoplease.com/ipa/A0762183.html')
    page_str = str(page.text)
    while (1): # continue until can't find a new city, then break (line 12)
        city_start = string.find(page_str, "<td align=\"left\" valign=\"top\">", city_start+1)
        if (city_start == -1):
            break
        city_end = string.find(page_str, "</td>", city_start)
        city_str = page_str[city_start+30:city_end]
        print city_str
        for x in range (0, 4):
            idx_start = string.find(page_str, "<td align=\"center\" valign=\"bottom\">", city_start)
            idx_end = string.find(page_str, "</td>", idx_start)
            idx_str = page_str[idx_start+35:idx_end]
            print idx_str
            city_start = idx_end

if __name__ == '__main__':
    main()
