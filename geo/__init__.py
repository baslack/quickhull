class Mesh():

    def __init__(self):
        self._verts = list()
        self._faces = list()

    def generate_obj(self, filename):
        """
        :type filename: str
        :param filename: filename of the obj
        :return: void
        """
        with open(filename, "w") as this_file:
            this_file.truncate()
            this_file.write("#Quickhull Project:\n#version 0.0\n#begin verticies\n")
            for v in self._verts:
                this_file.write("v {0} {1} {2}\n".format(v[0], v[1], v[2]))
            this_file.write("#begin faces\n")
            for f in self._faces:
                this_file.write("f")
                for v in f:
                    this_file.write(" {0}".format(v))
                this_file.write("\n")

    def add_vert(self, coords):
        """
        :type coords: tuple[float]
        :param coords: tuple of three floats
        :return: void
        """
        self._verts.append(coords)

    def add_face(self, verts):
        """
        :type verts: tuple[int]
        :param verts: tuple of three ints
        :return: void
        """
        self._faces.append(verts)

    def get_verts(self):
        """
        :rtype : list[tuple[int]]
        :return: list of tuples of vert coords
        """
        return self._verts

    def get_faces(self):
        """
        :rtype : list[tuple[int]]
        :return: list of tuples of vert indicies
        """

        return self._faces


if __name__ == "__main__":
    test_mesh = Mesh()
    test_mesh.add_vert((1.0,0.0,0.0))
    test_mesh.add_vert((0.0, 0.0, 1.0))
    test_mesh.add_vert((-1.0, 0.0, 0.0))
    test_mesh.add_vert((0.0, 0.0, -1.0))
    test_mesh.add_vert((0.0, 2.0, 0.0))
    test_mesh.add_face((1,5,2))
    test_mesh.add_face((2,5,3))
    test_mesh.add_face((3,5,4))
    test_mesh.add_face((4,5,1))
    test_mesh.add_face((1,2,3,4))
    test_mesh.generate_obj("pyramid.obj")
    these_verts = test_mesh.get_verts()
    print (these_verts[0][0])
    these_faces = test_mesh.get_faces()
    print (these_faces[0][0])



