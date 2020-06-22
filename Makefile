# Plot code
protein_domains_vs_string_degree.png : filtered_domains.txt
	python3 plot_code.py

# Parsing the protein domains dataset downloaded
# Removing header, proteins without domain information and retaining only protein names
filtered_domains.txt : domains.txt
	cat domains.txt | tail -n +2 | awk '!/^[[:blank:]]/' | awk 'BEGIN{FS = " ";}{print $$2}' > filtered_domains.txt

# Download the number of known protein domains per Ensembl ID
domains.txt : sig_edges.txt
	curl -L https://stockholmuniversity.box.com/shared/static/n8l0l1b3tg32wrzg2ensg8dnt7oua8ex --output domains.txt

# Cleaning and filtering for significant edges (combined score > 500)
sig_edges.txt : links.txt
	sed 's/9606\.//g' links.txt | awk '$$3 >= 500' | tail -n +2 > sig_edges.txt

# Unzip interaction network
links.txt : links.txt.gz
	gunzip -k links.txt.gz

# Downloading the Homo sapiens part of STRING
links.txt.gz :
	wget -O links.txt.gz https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz