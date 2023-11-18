"""
DType classes
-------------

The following are the classes of the corresponding NumPy dtype instances and
NumPy scalar types.  The classes can be used in ``isinstance`` checks and can
also be instantiated or used directly.  Direct use of these classes is not
typical, since their scalar counterparts (e.g. ``np.float64``) or strings
like ``"float64"`` can be used.

.. list-table::
    :header-rows: 1

    * - Group
      - DType class

    * - Boolean
      - ``BoolDType``

    * - Bit-sized integers
      - ``Int8DType``, ``UInt8DType``, ``Int16DType``, ``UInt16DType``,
        ``Int32DType``, ``UInt32DType``, ``Int64DType``, ``UInt64DType``

    * - C-named integers (may be aliases)
      - ``ByteDType``, ``UByteDType``, ``ShortDType``, ``UShortDType``,
        ``IntDType``, ``UIntDType``, ``LongDType``, ``ULongDType``,
        ``LongLongDType``, ``ULongLongDType``

    * - Floating point
      - ``Float16DType``, ``Float32DType``, ``Float64DType``,
        ``LongDoubleDType``

    * - Complex
      - ``Complex64DType``, ``Complex128DType``, ``CLongDoubleDType``

    * - Strings
      - ``BytesDType``, ``BytesDType``

    * - Times
      - ``DateTime64DType``, ``TimeDelta64DType``

    * - Others
      - ``ObjectDType``, ``VoidDType``
"""
import numpy as np

x = np.array([1, 2, 3, 4, 5, 7, 8, 9, 10],dtype=np.dtypes.BytesDType)

if __name__ == "main":
  print(x)
  print(x.dtype)
