
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_forms(url):
    """
    Get all form elements from the web page.
    :param url: Target URL.
    :return: List of form elements.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """
    Extract details from a form element.
    :param form: BeautifulSoup form element.
    :return: Dictionary containing form details.
    """
    details = {
        "action": form.attrs.get("action", "").strip(),
        "method": form.attrs.get("method", "get").lower(),
        "inputs": []
    }
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        details["inputs"].append({"type": input_type, "name": input_name})
    return details

def submit_form(url, form_details, payload):
    """
    Submit a form with a given payload.
    :param url: Target URL.
    :param form_details: Details of the form to be submitted.
    :param payload: Payload for testing vulnerabilities.
    :return: Response object.
    """
    target_url = urljoin(url, form_details["action"])
    data = {}
    for input_detail in form_details["inputs"]:
        if input_detail["type"] == "text" or input_detail["type"] == "search":
            data[input_detail["name"]] = payload
        elif input_detail["name"]:
            data[input_detail["name"]] = "test"
    
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    return requests.get(target_url, params=data)

def test_sql_injection(url):
    """
    Test SQL Injection vulnerability.
    :param url: Target URL.
    """
    sql_payload = "' OR '1'='1"
    forms = get_all_forms(url)
    print(f"[+] Found {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        response = submit_form(url, form_details, sql_payload)
        if "sql" in response.text.lower() or "syntax error" in response.text.lower():
            print(f"[!] SQL Injection vulnerability detected on {url}")
            print(f"    Form details: {form_details}")
        else:
            print(f"[-] No SQL Injection vulnerability found in the form: {form_details}")

def test_xss(url):
    """
    Test Cross-Site Scripting (XSS) vulnerability.
    :param url: Target URL.
    """
    xss_payload = "<script>alert('XSS')</script>"
    forms = get_all_forms(url)
    print(f"[+] Found {len(forms)} forms on {url}.")
    for form in forms:
        form_details = get_form_details(form)
        response = submit_form(url, form_details, xss_payload)
        if xss_payload in response.text:
            print(f"[!] XSS vulnerability detected on {url}")
            print(f"    Form details: {form_details}")
        else:
            print(f"[-] No XSS vulnerability found in the form: {form_details}")

if __name__ == "__main__":
    print("Web Application Vulnerability Scanner")
    target_url = input("Enter the target URL: ").strip()
    
    print("\n[1] Testing for SQL Injection...")
    test_sql_injection(target_url)
    
    print("\n[2] Testing for Cross-Site Scripting (XSS)...")
    test_xss(target_url)
    
    print("\nScanning completed.")
