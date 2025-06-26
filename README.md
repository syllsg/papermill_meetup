Pour exporter en html sans sauvergarder le notebook éxécuté : 
papermill -p year 2030 date_print.ipynb | jupyter-nbconvert --stdin --no-input --to html --output report_html