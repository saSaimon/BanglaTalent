#!/bin/bash

behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/landing_page_test.feature