#!/bin/bash

# Specify the path to your feature file
FEATURE_PATH="features/tests/landing_page_test.feature"

# Run tests on Chrome
(BROWSER=chrome HEADLESS=true behave $FEATURE_PATH) &

wait
# Run tests on Firefox
(BROWSER=firefox HEADLESS=true behave $FEATURE_PATH) &
wait
#Run tests on Edge
(BROWSER=edge HEADLESS=true behave $FEATURE_PATH) &
wait
#Run tests on Safari
#(BROWSER=safari behave $FEATURE_PATH) &
wait
