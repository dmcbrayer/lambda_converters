import getopt
import json
import math
import pdb
import sys

from OCC.Bnd import Bnd_Box
from OCC.BRepMesh import BRepMesh_IncrementalMesh
from OCC.BRepBndLib import brepbndlib_Add
from OCC.GProp import GProp_GProps
from OCC.gp import *
from OCC.BRepGProp import brepgprop_VolumeProperties
from OCC.STEPControl import STEPControl_Reader
from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity

def calculate_bnd_box(bbox):
  xmin, ymin, zmin, xmax, ymax, zmax = bbox.Get()
  x = xmax - xmin
  y = ymax - ymin
  z = zmax - zmin
  return {
    'volume': x * y * z,
    'x_length': x,
    'y_length': y,
    'z_length': z,
    'x_min': xmin,
    'x_max': xmax,
    'y_min': ymin,
    'y_max': ymax,
    'z_min': zmin,
    'z_max': zmax
  }

def calculate_volume(shape):
  props = GProp_GProps()
  brepgprop_VolumeProperties(shape, props)
  return props.Mass()

def analyze_file(filename):
  step_reader = STEPControl_Reader()
  status = step_reader.ReadFile(str(filename))
  result = None

  if status == IFSelect_RetDone:  # check status
    number_of_roots = step_reader.NbRootsForTransfer()
    ok = False
    i = 1

    while i <= number_of_roots and not ok:
      ok = step_reader.TransferRoot(i)
      i += 1

    if (not ok):
      return { 'error': 'Failed to find a suitable root for the STEP file' }

    number_of_shapes = step_reader.NbShapes()

    if (number_of_shapes > 1):
      return { 'error': 'Cannot handle more than one shape in a file' }

    aResShape = step_reader.Shape(1)

    # bounding box
    bbox = Bnd_Box()
    deflection = 0.01
    BRepMesh_IncrementalMesh(aResShape, deflection)

    brepbndlib_Add(aResShape, bbox)
    xmin, ymin, zmin, xmax, ymax, zmax = bbox.Get()

    bounding_box = calculate_bnd_box(bbox)

    result = {
      'x0': bounding_box['x_min'],
      'x1': bounding_box['x_max'],
      'y0': bounding_box['y_min'],
      'y1': bounding_box['y_max'],
      'z0': bounding_box['z_min'],
      'z1': bounding_box['z_max'],
      'length': bounding_box['x_length'],
      'width': bounding_box['z_length'],
      'height': bounding_box['y_length'],
      'volume': calculate_volume(aResShape)
    }

  else:
    result = { 'error': 'Cannot read file' }

  return result

def usage():
  print 'volume.py -f <inputfile>'
  sys.exit(0)

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "hf:", ["file="])
  except getopt.GetoptError:
    usage()

  filename = None
  for opt, arg in opts:
    if opt in ("-f", "--file"):
      filename = arg

  if filename != None:
    try:
      result = analyze_file(filename)
    except RuntimeError as e:
      result = { 'error': e.message, 'filename': filename }

    print(json.dumps(result))

  else:
    result = { 'error': 'No filename provided' }
    print(json.dumps(result))

  sys.exit(0)

if __name__ == '__main__':
  main(sys.argv[1:])
