docker build -t juankanh/jmeter-docker .
docker push juankanh/jmeter-docker:latest


--crear un pod OK
--crear deployment OK
--añadir un pvc OK
--añadir configmap 


Create ConfigMap from files :

kubectl create configmap <CONFIGMAP_NAME>  --from-file=<FOLDER_WITH_THE_FILES>