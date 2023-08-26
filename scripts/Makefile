all:
	installReq
	downloadRes
	unzipRes

installReq:
	conda env create -f ./environment.yml -n gis

downloadRes:
	python3 ./scripts/downloadFile.py

unzipRes:
	python3 ./scripts/unzipFile.py

cleanAll:
	rm -rf ./datas/*
	rm -rf ./outputs/*

cleanOutput:
	rm -rf ./outputs/*