"""
Python library that provides wrappers around the Ristretto group operations in libsodium.

This library exports all libsodium methods related to the Ristretto group or RNG, including
all `crypto_scalarmult*` methods and the `randombytes*` methods.
"""
from __future__ import annotations
import doctest

try:
    from rbcl import _sodium
except: # pylint: disable=W0702 # pragma: no cover
    # Support for direct invocation in order to execute doctests.
    import _sodium

crypto_scalarmult_ristretto255_BYTES: int = \
    _sodium.lib.crypto_scalarmult_ristretto255_bytes()
crypto_scalarmult_ristretto255_SCALARBYTES: int = \
    _sodium.lib.crypto_scalarmult_ristretto255_scalarbytes()
crypto_core_ristretto255_BYTES: int = \
    _sodium.lib.crypto_core_ristretto255_bytes()
crypto_core_ristretto255_HASHBYTES: int = \
    _sodium.lib.crypto_core_ristretto255_hashbytes()
crypto_core_ristretto255_NONREDUCEDSCALARBYTES: int = \
    _sodium.lib.crypto_core_ristretto255_nonreducedscalarbytes()
crypto_core_ristretto255_SCALARBYTES: int = \
    _sodium.lib.crypto_core_ristretto255_scalarbytes()
randombytes_SEEDBYTES: int = \
    _sodium.lib.randombytes_seedbytes()


def crypto_core_ristretto255_is_valid_point(p):  # (const unsigned char *p);
    """
    Check if ``p`` represents a point on the ristretto255 curve, in canonical
    form, on the main subgroup, and that the point doesn't have a small order.

    :param p: a :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
              representing a point on the ristretto255 curve
    :type p: bytes
    :return: point validity
    :rtype: bool
    """
    if not isinstance(p, bytes) or len(p) != crypto_core_ristretto255_BYTES:
        raise TypeError(
            "Point must be a " + str(crypto_core_ristretto255_BYTES) +
            "long bytes sequence"
        )  # pragma: no cover

    rc = _sodium.lib.crypto_core_ristretto255_is_valid_point(p)
    return rc == 1


# (unsigned char *r, const unsigned char *p, const unsigned char *q);
def crypto_core_ristretto255_add(p, q):
    """
    Add two points on the ristretto255 curve.

    :param p: a :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
              representing a point on the ristretto255 curve
    :type p: bytes
    :param q: a :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
              representing a point on the ristretto255 curve
    :type q: bytes
    :return: a point on the ristretto255 curve represented as
             a :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(p, bytes) or len(p) != crypto_core_ristretto255_BYTES\
       or not isinstance(q, bytes) or len(q) != crypto_core_ristretto255_BYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_BYTES
        )  # pragma: no cover

    r = _sodium.ffi.new("unsigned char[]", crypto_core_ristretto255_BYTES)

    _sodium.lib.crypto_core_ristretto255_add(r, p, q)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_BYTES)[:]


# (unsigned char *r, const unsigned char *p, const unsigned char *q);
def crypto_core_ristretto255_sub(p, q):
    """
    Subtract a point from another on the ristretto255 curve.

    :param p: a :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
              representing a point on the ristretto255 curve
    :type p: bytes
    :param q: a :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
              representing a point on the ristretto255 curve
    :type q: bytes
    :return: a point on the ristretto255 curve represented as
             a :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(p, bytes) or len(p) != crypto_core_ristretto255_BYTES\
       or not isinstance(q, bytes) or len(q) != crypto_core_ristretto255_BYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_BYTES
        )  # pragma: no cover

    r = _sodium.ffi.new("unsigned char[]", crypto_core_ristretto255_BYTES)

    _sodium.lib.crypto_core_ristretto255_sub(r, p, q)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_BYTES)[:]


# (unsigned char *p, const unsigned char *r);
def crypto_core_ristretto255_from_hash(h):
    """
    Map a 64-byte vector ``h`` (usually the output of a hash function) to a ristretto255
    group element (a point), and output its representation in bytes.

    :param h: a :py:data:`.crypto_core_ristretto255_HASHBYTES`
              long bytes sequence ideally representing a hash digest
    :type h: bytes

    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(h, bytes) or len(
            h) != crypto_core_ristretto255_HASHBYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_HASHBYTES
        )  # pragma: no cover

    r = _sodium.ffi.new("unsigned char[]", crypto_core_ristretto255_BYTES)

    _sodium.lib.crypto_core_ristretto255_from_hash(r, h)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_BYTES)[:]


def crypto_core_ristretto255_random():  # (unsigned char *p);
    """
    Returns a ristretto255 group element (point).

    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_BYTES` long bytes sequence
    :rtype: bytes
    """

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_random(r)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


def crypto_core_ristretto255_scalar_random():  # (unsigned char *r);
    """
    Returns a :py:data:`.crypto_core_ristretto255_SCALARBYTES` byte long
    representation of the scalar in the ``[0..L]`` interval, ``L`` being the
    order of the group ``(2^252 + 27742317777372353535851937790883648493)``.

    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_SCALARBYTES` long bytes sequence
    :rtype: bytes
    """

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_scalar_random(r)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


# (unsigned char *recip, const unsigned char *s);
def crypto_core_ristretto255_scalar_invert(p):
    """
    Return the multiplicative inverse of integer ``s`` modulo ``L``,
    i.e an integer ``i`` such that ``s * i = 1 (mod L)``, where ``L``
    is the order of the main subgroup.

    Raises a ``RuntimeError`` if ``s`` is the integer zero.

    :param s: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type s: bytes
    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_SCALARBYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(p, bytes) or len(
            p) != crypto_core_ristretto255_SCALARBYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_SCALARBYTES
        )  # pragma: no cover

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_scalar_invert(r, p)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


# (unsigned char *neg, const unsigned char *s);
def crypto_core_ristretto255_scalar_negate(p):
    """
    Return the integer ``n`` such that ``s + n = 0 (mod L)``, where ``L``
    is the order of the main subgroup.

    :param s: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type s: bytes
    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_SCALARBYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(p, bytes) or len(
            p) != crypto_core_ristretto255_SCALARBYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_SCALARBYTES
        )  # pragma: no cover

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_scalar_negate(r, p)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


# (unsigned char *comp, const unsigned char *s);
def crypto_core_ristretto255_scalar_complement(p):
    """
    Return the complement of integer ``s`` modulo ``L``, i.e. an integer
    ``c`` such that ``s + c = 1 (mod L)``, where ``L`` is the order of
    the main subgroup.

    :param s: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type s: bytes
    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_SCALARBYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(p, bytes) or len(
            p) != crypto_core_ristretto255_SCALARBYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_SCALARBYTES
        )  # pragma: no cover

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_scalar_complement(r, p)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


# (unsigned char *z, const unsigned char *x, const unsigned char *y);
def crypto_core_ristretto255_scalar_add(p, q):
    """
    Add integers ``p`` and ``q`` modulo ``L``, where ``L`` is the order of
    the main subgroup.

    :param p: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type p: bytes
    :param q: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type q: bytes
    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_SCALARBYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(
            p, bytes) or len(p) != crypto_core_ristretto255_SCALARBYTES or not isinstance(
            q, bytes) or len(q) != crypto_core_ristretto255_SCALARBYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_SCALARBYTES
        )  # pragma: no cover

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_scalar_add(r, p, q)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


# (unsigned char *z, const unsigned char *x, const unsigned char *y);
def crypto_core_ristretto255_scalar_sub(p, q):
    """
    Subtract integers ``p`` and ``q`` modulo ``L``, where ``L`` is the
    order of the main subgroup.

    :param p: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type p: bytes
    :param q: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type q: bytes
    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_SCALARBYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(
            p, bytes) or len(p) != crypto_core_ristretto255_SCALARBYTES or not isinstance(
            q, bytes) or len(q) != crypto_core_ristretto255_SCALARBYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_SCALARBYTES
        )  # pragma: no cover

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_scalar_sub(r, p, q)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


# (unsigned char *z, const unsigned char *x, const unsigned char *y);
def crypto_core_ristretto255_scalar_mul(p, q):
    """
    Multiply integers ``p`` and ``q`` modulo ``L``, where ``L`` is the
    order of the main subgroup.

    :param p: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type p: bytes
    :param q: a :py:data:`.crypto_core_ristretto255_SCALARBYTES`
              long bytes sequence representing an integer
    :type q: bytes
    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_SCALARBYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(
            p, bytes) or len(p) != crypto_core_ristretto255_SCALARBYTES or not isinstance(
            q, bytes) or len(q) != crypto_core_ristretto255_SCALARBYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_SCALARBYTES
        )  # pragma: no cover

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_scalar_mul(r, p, q)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


# (unsigned char *r, const unsigned char *s);
def crypto_core_ristretto255_scalar_reduce(p):
    """
    Reduce integer ``s`` to ``s`` modulo ``L``, where ``L`` is the order
    of the main subgroup.

    :param s: a :py:data:`.crypto_core_ristretto255_NONREDUCEDSCALARBYTES`
              long bytes sequence representing an integer
    :type s: bytes
    :return: an integer represented as a
              :py:data:`.crypto_core_ristretto255_SCALARBYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(p, bytes) or len(
            p) != crypto_core_ristretto255_SCALARBYTES:
        raise TypeError(
            "Each integer must be a {} long bytes sequence"
                % crypto_core_ristretto255_SCALARBYTES
        )  # pragma: no cover

    r = _sodium.ffi.new(
        "unsigned char[]",
        crypto_core_ristretto255_SCALARBYTES)

    _sodium.lib.crypto_core_ristretto255_scalar_reduce(r, p)

    return _sodium.ffi.buffer(r, crypto_core_ristretto255_SCALARBYTES)[:]


def crypto_scalarmult_ristretto255_base(n):
    """
    Computes and returns the scalar product of a standard group element and an
    integer ``n`` on the ristretto255 curve.

    :param n: a :py:data:`.crypto_scalarmult_ristretto255_SCALARBYTES` long bytes
              sequence representing a scalar
    :type n: bytes
    :return: a point on the ristretto255 curve, represented as a
             :py:data:`.crypto_scalarmult_ristretto255_BYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(n, bytes) or len(
            n) != crypto_scalarmult_ristretto255_SCALARBYTES:
        raise TypeError(
            "Input must be a {} long bytes sequence"
                % crypto_scalarmult_ristretto255_SCALARBYTES
        )  # pragma: no cover

    q = _sodium.ffi.new(
        "unsigned char[]",
        crypto_scalarmult_ristretto255_BYTES)

    if _sodium.lib.crypto_scalarmult_ristretto255_base(q, n) == -1:
        raise RuntimeError(
            "`n` cannot be larger than the size of the group or g^n is the identity element"
        )  # pragma: no cover

    return _sodium.ffi.buffer(q, crypto_scalarmult_ristretto255_BYTES)[:]


def crypto_scalarmult_ristretto255(n, p):
    """
    Computes and returns the scalar product of a *clamped* integer ``n``
    and the given group element on the ristretto255 curve.
    The scalar is clamped, as done in the public key generation case,
    by setting to zero the bits in position [0, 1, 2, 255] and setting
    to one the bit in position 254.

    :param n: a :py:data:`.crypto_scalarmult_ristretto255_SCALARBYTES` long bytes
              sequence representing a scalar
    :type n: bytes
    :param p: a :py:data:`.crypto_scalarmult_ristretto255_BYTES` long bytes sequence
              representing a point on the ristretto255 curve
    :type p: bytes
    :return: a point on the ristretto255 curve, represented as a
             :py:data:`.crypto_scalarmult_ristretto255_BYTES` long bytes sequence
    :rtype: bytes
    """
    if not isinstance(n, bytes) or len(
            n) != crypto_scalarmult_ristretto255_SCALARBYTES:
        raise TypeError(
            "Input must be a {} long bytes sequence"
                % crypto_scalarmult_ristretto255_SCALARBYTES
        )

    if not isinstance(p, bytes) or len(
            p) != crypto_scalarmult_ristretto255_BYTES:
        raise TypeError(
            "Input must be a {} long bytes sequence"
                % crypto_scalarmult_ristretto255_BYTES
        )

    q = _sodium.ffi.new(
        "unsigned char[]",
        crypto_scalarmult_ristretto255_BYTES)

    if _sodium.lib.crypto_scalarmult_ristretto255(q, n, p) == -1:
        raise RuntimeError(
            "`n` cannot be larger than the size of the group or p^n is the identity element")

    return _sodium.ffi.buffer(q, crypto_scalarmult_ristretto255_BYTES)[:]


def randombytes(size):
    """
    Returns ``size`` number of random bytes from a cryptographically secure
    random source.

    :param size: int
    :rtype: bytes
    """
    buf = _sodium.ffi.new("unsigned char[]", size)
    _sodium.lib.randombytes(buf, size)
    return _sodium.ffi.buffer(buf, size)[:]


def randombytes_buf_deterministic(size, seed):
    """
    Returns ``size`` number of deterministically generated pseudorandom bytes
    from a seed

    :param size: int
    :param seed: bytes
    :rtype: bytes
    """
    if len(seed) != randombytes_SEEDBYTES:
        raise TypeError(
            "Deterministic random bytes must be generated from 32 bytes"
        )

    buf = _sodium.ffi.new("unsigned char[]", size)
    _sodium.lib.randombytes_buf_deterministic(buf, size, seed)
    return _sodium.ffi.buffer(buf, size)[:]

# Initializes sodium, picking the best implementations available for this
# machine.


def _sodium_init():
    if _sodium.lib.sodium_init() == -1:
        raise RuntimeError(
            "libsodium error during initialization")  # pragma: no cover


_sodium.ffi.init_once(_sodium_init, "libsodium")

if __name__ == "__main__":
    doctest.testmod()  # pragma: no cover
