all:
	installReq
	downloadRes
	unzipRes

installReq:
	pip3 install -r requirements.txt

downloadRes:
	python3 ./scripts/downloadFile.py

unzipRes:
	python3 ./scripts/unzipFile.py

cleanAll:
	rm -rf ./datas/*
	rm -rf ./outputs/*

cleanOutput:
	rm -rf ./outputs/*