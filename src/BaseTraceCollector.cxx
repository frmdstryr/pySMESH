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

#include <BaseTraceCollector.hxx>

PYBIND11_MODULE(BaseTraceCollector, mod) {

	// CLASSES
	py::class_<BaseTraceCollector> cls_BaseTraceCollector(mod, "BaseTraceCollector", "See derived Classes in SALOMELocalTrace for usage without CORBA, see derived Classes in SALOMETraceCollector for usage with CORBA.");

}
