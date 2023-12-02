import webbrowser
favolite_list={
    "google":"https://www.google.com.eg/?hl=ar",
    "youtube":"https://www.youtube.com/",
    "facebook":"https://web.facebook.com/?_rdc=1&_rdr"
}
def firefox(website_name):
    website_name=website_name.strip().casefold()
    if website_name not in favolite_list.keys():
        print("this website dose not exist in favorite list")
    else:
        webbrowser.get('firefox').open_new_tab(favolite_list[website_name])
        print("this website is opend successfully")