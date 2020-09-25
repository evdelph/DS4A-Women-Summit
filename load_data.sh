cd data
for week_num in {01..13}
do
    week_num_int=$(echo $week_num | sed 's/^0*//')
    wget https://www2.census.gov/programs-surveys/demo/datasets/hhp/2020/wk${week_num_int}/HPS_Week${week_num}_PUF_CSV.zip
    unzip HPS_Week${week_num}_PUF_CSV.zip -x *repwgt*
done