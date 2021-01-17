/*
This file is part of pySMESH which provides Python bindings to SMESH.

Copyright (C) 2016-2018 Laughlin Research, LLC
Copyright (C) 2019-2021 Trevor Laughlin and the pySMESH contributors

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/
#include <pySMESH_Common.hxx>

#include <Driver_SMDS_Mesh.h>
#include <Driver_Mesh.h>
#include <DriverSTL_R_SMDS_Mesh.h>
#include <DriverSTL_W_SMDS_Mesh.h>

PYBIND11_MODULE(DriverSTL, mod) {

	// IMPORT
	py::module::import("SMESH.Driver");

	// CLASSES
	py::class_<DriverSTL_R_SMDS_Mesh, Driver_SMDS_Mesh> cls_DriverSTL_R_SMDS_Mesh(mod, "DriverSTL_R_SMDS_Mesh", "None");
	cls_DriverSTL_R_SMDS_Mesh.def(py::init<>());
	cls_DriverSTL_R_SMDS_Mesh.def("Perform", (Driver_Mesh::Status (DriverSTL_R_SMDS_Mesh::*)()) &DriverSTL_R_SMDS_Mesh::Perform, "None");
	cls_DriverSTL_R_SMDS_Mesh.def("SetIsCreateFaces", [](DriverSTL_R_SMDS_Mesh &self) -> void { return self.SetIsCreateFaces(); });
	cls_DriverSTL_R_SMDS_Mesh.def("SetIsCreateFaces", (void (DriverSTL_R_SMDS_Mesh::*)(const bool)) &DriverSTL_R_SMDS_Mesh::SetIsCreateFaces, "None", py::arg("theIsCreate"));
	cls_DriverSTL_R_SMDS_Mesh.def("GetName", (std::string (DriverSTL_R_SMDS_Mesh::*)() const ) &DriverSTL_R_SMDS_Mesh::GetName, "None");

	py::class_<DriverSTL_W_SMDS_Mesh, Driver_SMDS_Mesh> cls_DriverSTL_W_SMDS_Mesh(mod, "DriverSTL_W_SMDS_Mesh", "Writer of a mesh in STL (STereoLithography) file format.");
	cls_DriverSTL_W_SMDS_Mesh.def(py::init<>());
	cls_DriverSTL_W_SMDS_Mesh.def("Perform", (Driver_Mesh::Status (DriverSTL_W_SMDS_Mesh::*)()) &DriverSTL_W_SMDS_Mesh::Perform, "None");
	cls_DriverSTL_W_SMDS_Mesh.def("SetIsAscii", [](DriverSTL_W_SMDS_Mesh &self) -> void { return self.SetIsAscii(); });
	cls_DriverSTL_W_SMDS_Mesh.def("SetIsAscii", (void (DriverSTL_W_SMDS_Mesh::*)(const bool)) &DriverSTL_W_SMDS_Mesh::SetIsAscii, "None", py::arg("theIsAscii"));
	cls_DriverSTL_W_SMDS_Mesh.def("SetName", (void (DriverSTL_W_SMDS_Mesh::*)(const std::string)) &DriverSTL_W_SMDS_Mesh::SetName, "None", py::arg("name"));

}
