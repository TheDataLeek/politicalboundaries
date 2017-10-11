
slides:
	jupyter nbconvert --to slides politicalboundaries.ipynb --reveal-prefix '/presentations/reveal.js-3.5.0'
	rsync -uaz --progress * root@dataleek.io:/var/www/html/presentations/politicalboundaries/
