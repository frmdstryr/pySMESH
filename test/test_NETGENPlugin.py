# This file is part of pySMESH which provides Python bindings to SMESH.
#
# Copyright (C) 2016-2018 Laughlin Research, LLC
# Copyright (C) 2019-2021 Trevor Laughlin and the pySMESH contributors
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
import unittest

from OCCT.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCCT.TopAbs import TopAbs_EDGE
from OCCT.TopExp import TopExp_Explorer
from SMESH.NETGENPlugin import (NETGENPlugin_SimpleHypothesis_3D, NETGENPlugin_NETGEN_2D3D,
                                NETGENPlugin_SimpleHypothesis_2D, NETGENPlugin_NETGEN_2D)
from SMESH.SMESH import SMESH_Gen
from SMESH.StdMeshers import StdMeshers_LocalLength, StdMeshers_Regular_1D


class Test_NETGENPlugin(unittest.TestCase):
    """
    Test for NETGENPlugin.
    """

    def test_Box3D(self):
        """
        Test a tetrahedral mesh of a simple solid box.
        """
        box = BRepPrimAPI_MakeBox(10, 10, 10).Solid()

        gen = SMESH_Gen()
        mesh = gen.CreateMesh(True)

        hyp = NETGENPlugin_SimpleHypothesis_3D(0, gen)
        hyp.SetLocalLength(1.0)

        NETGENPlugin_NETGEN_2D3D(1, 0, gen)

        mesh.ShapeToMesh(box)
        mesh.AddHypothesis(box, 0)
        mesh.AddHypothesis(box, 1)

        success = gen.Compute(mesh, box)
        self.assertTrue(success)

        self.assertEqual(mesh.NbTetras(), 4741)
        self.assertEqual(mesh.NbNodes(), 1185)

    def test_Box2DTri(self):
        """
        Test a triangular mesh of a simple box.
        """
        box = BRepPrimAPI_MakeBox(10, 10, 10).Solid()

        gen = SMESH_Gen()
        mesh = gen.CreateMesh(True)

        hyp = NETGENPlugin_SimpleHypothesis_2D(0, gen)
        hyp.SetLocalLength(1.0)

        NETGENPlugin_NETGEN_2D(1, gen)

        mesh.ShapeToMesh(box)
        mesh.AddHypothesis(box, 0)
        mesh.AddHypothesis(box, 1)

        success = gen.Compute(mesh, box)
        self.assertTrue(success)

        self.assertEqual(mesh.NbTriangles(), 1422)
        self.assertEqual(mesh.NbNodes(), 713)

    def test_Box2DQuad(self):
        """
        Test a quadrilateral mesh of a simple box.
        """
        box = BRepPrimAPI_MakeBox(10, 10, 10).Solid()

        gen = SMESH_Gen()
        mesh = gen.CreateMesh(True)

        hyp = NETGENPlugin_SimpleHypothesis_2D(0, gen)
        hyp.SetAllowQuadrangles(True)
        hyp.SetLocalLength(1.0)

        NETGENPlugin_NETGEN_2D(1, gen)

        mesh.ShapeToMesh(box)
        mesh.AddHypothesis(box, 0)
        mesh.AddHypothesis(box, 1)

        success = gen.Compute(mesh, box)
        self.assertTrue(success)

        self.assertEqual(mesh.NbTriangles(), 0)
        self.assertEqual(mesh.NbQuadrangles(), 600)
        self.assertEqual(mesh.NbNodes(), 602)

    def test_LocalEdgeLength(self):
        """
        Test a mesh on a box with a local edge length enforced on one edge.
        """
        box = BRepPrimAPI_MakeBox(10, 10, 10).Solid()
        edge = TopExp_Explorer(box, TopAbs_EDGE).Current()

        gen = SMESH_Gen()
        mesh = gen.CreateMesh(True)

        hyp3d = NETGENPlugin_SimpleHypothesis_3D(0, gen)
        hyp3d.SetLocalLength(1.0)
        NETGENPlugin_NETGEN_2D3D(1, gen)

        hyp1d = StdMeshers_LocalLength(2, gen)
        hyp1d.SetLength(0.1)
        StdMeshers_Regular_1D(3, gen)

        mesh.ShapeToMesh(box)
        mesh.AddHypothesis(box, 0)
        mesh.AddHypothesis(box, 1)
        mesh.AddHypothesis(edge, 2)
        mesh.AddHypothesis(edge, 3)

        success = gen.Compute(mesh, box)
        self.assertTrue(success)

        self.assertEqual(mesh.NbTetras(), 31547)
        self.assertEqual(mesh.NbNodes(), 6205)


if __name__ == '__main__':
    unittest.main()
