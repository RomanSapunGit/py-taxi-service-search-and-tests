from django.test import TestCase

from taxi.forms import DriverLicenseUpdateForm


class FormTestClass(TestCase):
    def test_validate_license_number_works_correctly(self):
        invalid_inputs = ["abc", "ABCDEFGH", "123DEFGH"]
        valid_input = {"license_number": "ABC12345"}

        for input_str in invalid_inputs:
            assert_form_validity(
                self,
                DriverLicenseUpdateForm,
                {"license_number": input_str},
                should_be_valid=False
            )

        assert_form_validity(
            self,
            DriverLicenseUpdateForm,
            valid_input,
            should_be_valid=True
        )


def assert_form_validity(testcase, form_class, data, should_be_valid):
    form = form_class(data=data)
    if should_be_valid:
        testcase.assertTrue(
            form.is_valid(),
            f"Form should be valid for data: {data}, "
            f"but got errors: {form.errors}"
        )
    else:
        testcase.assertFalse(
            form.is_valid(),
            f"Form should be invalid for data: {data}"
        )
