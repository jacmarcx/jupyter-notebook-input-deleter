def jupyter_input_deleter(filename):
    '''
    Takes the HTML file from an exported Jupyter Notebook
    and strips out all of the code input div tags for cleaner
    documents for sharing with non-data science folks
    # this works for jupyterlab 4.3.6
    '''

    from bs4 import BeautifulSoup
    import re
    soup = BeautifulSoup(open(filename),'html.parser')

    #strip input code (if not markdown)
    for div in soup.find_all('div',attrs={'class':re.compile(r'jp-Cell jp-CodeCell')}):
        div.find('div', attrs={'class':'jp-Cell-inputWrapper'}).decompose()
    
    #strip output box cell id number
    for div in soup.find_all('div',attrs={'class':'jp-OutputPrompt jp-OutputArea-prompt'}):
        div.decompose()
    
    html_file = open(f'{filename[0:-5]}-codeless.html', 'w')
    html_file.write(str(soup))
    html_file.close()
