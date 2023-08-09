#!/usr/bin/python3
""" Test BaseModel module """

import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def setUp(self):
        self.basemodel = BaseModel()
        self.basemodel_1 = BaseModel()

    def test_doc(self):
        """test doc"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_save_BaseModel(self):
        """test save_BaseModel"""

        self.basemodel.save()
        self.assertEqual(self.basemodel.created_at, self.basemodel.updated_at)

    def test_basemodel_id(self):
        """test basemodel id"""
        self.assertNotEqual(self.basemodel.id, self.basemodel_1.id)

    def test_basemodel_name(self):
        """test basemodel name"""
        self.basemodel.name = "model_1"
        self.basemodel_1.name = "model_2"
        self.assertTrue(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel_1, "name"))
        self.assertNotEqual(self.basemodel.name, self.basemodel_1.name)

    def test_instance(self):
        """test instance"""
        self.assertTrue(isinstance(self.basemodel, BaseModel))
        self.assertTrue(isinstance(self.basemodel_1, BaseModel))

    def test_kwarg(self):
        """test kwqrg"""
        basemodel = BaseModel(name="base")
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertFalse(hasattr(basemodel, "id"))
        self.assertFalse(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "name"))
        self.assertFalse(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))


if __name__ == "__main__":
    unittest.main()
