import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch page: {e}")
        return None

def parse_quotes(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    quotes = soup.find_all('div', class_='quote')

    data = []
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        data.append({'text': text, 'author': author, 'tags': ', '.join(tags)})

    return data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def scrape_quotes():
    url = url_entry.get()
    pages = int(pages_entry.get())

    all_data = []
    for page in range(1, pages + 1):
        html_content = fetch_page(f"{url}/page/{page}")
        if html_content:
            page_data = parse_quotes(html_content)
            all_data.extend(page_data)
        else:
            return

    for quote in all_data:
        tree.insert("", "end", values=(quote['text'], quote['author'], quote['tags']))

def save_data():
    data = []
    for row in tree.get_children():
        values = tree.item(row)['values']
        data.append({'text': values[0], 'author': values[1], 'tags': values[2]})

    if not data:
        messagebox.showwarning("Warning", "No data to save")
        return

    file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file:
        save_to_csv(data, file)
        messagebox.showinfo("Success", f"Data saved to {file}")

# Create the GUI
root = tk.Tk()
root.title("Web Scraping App")

# URL Input
tk.Label(root, text="URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)
url_entry.insert(0, "http://quotes.toscrape.com")

# Pages Input
tk.Label(root, text="Pages to scrape:").grid(row=1, column=0, padx=10, pady=10)
pages_entry = tk.Entry(root, width=5)
pages_entry.grid(row=1, column=1, padx=10, pady=10)
pages_entry.insert(0, "1")

# Scrape Button
scrape_button = tk.Button(root, text="Scrape", command=scrape_quotes)
scrape_button.grid(row=2, column=0, columnspan=2, pady=10)

# Treeview for displaying data
columns = ("text", "author", "tags")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("text", text="Quote")
tree.heading("author", text="Author")
tree.heading("tags", text="Tags")
tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Save Button
save_button = tk.Button(root, text="Save to CSV", command=save_data)
save_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
