env:
	conda env create -f environment.yml
html:
	jupyter-book build .
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html; python -m http.server
clean:
	rm -f figurs/*
	rm -f audio/*
	rm -r _build/*