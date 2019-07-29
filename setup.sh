mkdir data
mkdir data/raw
source ./build_docker_image.sh
unzip ./sample_submission.csv.zip
unzip ./test_identity.csv.zip
unzip ./test_transaction.csv.zip
unzip ./train_identity.csv.zip
unzip ./train_transaction.csv.zip

mv *zip data/raw
mv *csv data/raw
chmod 660 data/raw/*



