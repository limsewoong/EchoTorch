# -*- coding: utf-8 -*-
#
# File : echotorch/matrices.py
# Description : EchoTorch matrix creation utility functions.
# Date : 30th of March, 2021
#
# This file is part of EchoTorch.  EchoTorch is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Nils Schaetti, University of Neuchâtel <nils.schaetti@unine.ch>,
# University of Geneva <nils.schaetti@unige.ch>

# Imports
import torch
import echotorch.utils.matrix_generation


# Cycle matrix with jumps generator
def cycle_with_jumps_generator(connectivity=1.0, spectra_radius=1.0, apply_spectral_radius=False, scale=1.0,
                               cycle_weight=1.0, jump_weight=1.0, jump_size=2.0):
    """
    Cycle matrix with jumps generator
    """
    return echotorch.utils.matrix_generation.matrix_factory.get_generator(
        "cycle_with_jumps",
        connectivity=connectivity,
        spectra_radius=spectra_radius,
        apply_spectral_radius=apply_spectral_radius,
        scale=scale,
        cycle_weight=cycle_weight,
        jump_weight=jump_weight,
        jump_size=jump_size
    )
# end cycle_with_jumps_generator


# Generate cycle matrix with jumps (Rodan and Tino, 2012)
def cycle_with_jumps(*size, connectivity=1.0, spectra_radius=1.0, apply_spectral_radius=False, scale=1.0,
                     cycle_weight=1.0, jump_weight=1.0, jump_size=2.0, dtype=None):
    """
    Generate cycle matrix with jumps (Rodan and Tino, 2012)
    """
    # Cycle with jumps generator
    matrix_generator = cycle_with_jumps_generator(
        connectivity=connectivity,
        spectra_radius=spectra_radius,
        apply_spectral_radius=apply_spectral_radius,
        scale=scale,
        cycle_weight=cycle_weight,
        jump_weight=jump_weight,
        jump_size=jump_size
    )

    # Generate matrix
    return matrix_generator.generate(size=size, dtype=dtype)
# end cycle_with_jumps


# Matlab loader generator
def matlab_generator(file_path, entity_name, shape=None, spectral_radius=1.0, apply_spectral_radius=False, scale=1.0):
    """
    Matlab loader generator
    """
    return echotorch.utils.matrix_generation.matrix_factory.get_generator(
        "matlab",
        file_path=file_path,
        entity_name=entity_name,
        shape=shape,
        spectral_radius=spectral_radius,
        scale=scale,
        apply_spectral_radius=apply_spectral_radius
    )
# end matlab_generator


# Load matrix from matlab file
def matlab(file_path, entity_name, *size, spectral_radius=1.0, apply_spectral_radius=False, scale=1.0, dtype=None):
    """
    Load matrix from matlab file
    """
    matrix_generator = matlab_generator(
        file_path=file_path,
        entity_name=entity_name,
        shape=size,
        spectral_radius=spectral_radius,
        scale=scale,
        apply_spectral_radius=apply_spectral_radius
    )

    # Generate matrix
    return matrix_generator.generate(size=size, dtype=dtype)
# end matlab


# Normal matrix generator
def normal_generator(connectivity=1.0, spectral_radius=1.0, scale=1.0, mean=0.0, std=1.0, minimum_edges=0,
           apply_spectral_radius=False):
    """
    Normal matrix generator
    """
    return echotorch.utils.matrix_generation.matrix_factory.get_generator(
        "normal",
        connectivity=connectivity,
        spectral_radius=spectral_radius,
        scale=scale,
        apply_spectral_radius=apply_spectral_radius,
        mean=mean,
        std=std,
        minimum_edges=minimum_edges
    )
# end normal_generator


# Normal matrix generation
def normal(*size, connectivity=1.0, spectral_radius=1.0, scale=1.0, mean=0.0, std=1.0, minimum_edges=0,
           apply_spectral_radius=False, dtype=None):
    """
    Normal matrix generation
    """
    # Matrix generator
    matrix_generator = normal_generator(
        connectivity=connectivity,
        spectral_radius=spectral_radius,
        scale=scale,
        apply_spectral_radius=apply_spectral_radius,
        mean=mean,
        std=std,
        minimum_edges=minimum_edges
    )

    # Generate matrix
    return matrix_generator.generate(size=size, dtype=dtype)
# end normal


# Uniform matrix generator
def uniform_generator(connectivity=1.0, spectral_radius=1.0, scale=1.0, input_set=[1.0, -1.0], minimum_edges=0,
            min=-1.0, max=1.0, apply_spectral_radius=False):
    """
    Uniform matrix generator
    """
    return echotorch.utils.matrix_generation.matrix_factory.get_generator(
        "uniform",
        connectivity=connectivity,
        spectral_radius=spectral_radius,
        scale=scale,
        input_set=input_set,
        minimum_edges=minimum_edges,
        min=min,
        max=max,
        apply_spectral_radius=apply_spectral_radius
    )
# end uniform_generator


# Uniform matrix generation
def uniform(*size, connectivity=1.0, spectral_radius=1.0, scale=1.0, input_set=[1.0, -1.0], minimum_edges=0,
            min=-1.0, max=1.0, apply_spectral_radius=False, dtype=None):
    """
    Uniform matrix generation
    :param connectivity:
    :param spectral_radius:
    :param scale:
    :param input_set:
    :param minimum_edges:
    :param min:
    :param max:
    :param apply_spectral_radius:
    :param dtype:
    """
    # Matrix generator
    matrix_generator = uniform_generator(
        connectivity=connectivity,
        spectral_radius=spectral_radius,
        scale=scale,
        input_set=input_set,
        minimum_edges=minimum_edges,
        min=min,
        max=max,
        apply_spectral_radius=apply_spectral_radius
    )

    # Generate matrix
    return matrix_generator.generate(size=size, dtype=dtype)
# end uniform

