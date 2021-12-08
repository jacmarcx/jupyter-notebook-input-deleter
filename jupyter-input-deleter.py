def jupyter_input_deleter(filename):
    '''
    Takes the HTML file from an exported Jupyter Notebook
    and strips out all of the code input div tags for cleaner
    documents for sharing with non-data science folks
    '''

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(open(filename),'html.parser')
    
    #strip input code
    for div in soup.find_all('div',attrs={'class':'input'}):
        div.decompose()
    
    #strip output box cell id number
    for div in soup.find_all('div',attrs={'class':'prompt output_prompt'}):
        div.decompose()
    
    html_file = open(f'{filename[0:-5]}-codeless.html', 'w')
    html_file.write(str(soup))
    html_file.close()
