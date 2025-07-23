#!/bin/bash

sed -e 's/USA/Togo/g' -e 's/Canada/China/g' -e 's/Dallas/Allen/g'  data.csv > data6.csv

echo 'data processed successffully'
