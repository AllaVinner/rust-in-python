use pyo3::prelude::*;
use numpy::ndarray::{Array1, ArrayD, ArrayView1, ArrayViewD, ArrayViewMutD, Zip};
use numpy::{
    datetime::{units, Timedelta},
    Complex64, IntoPyArray, PyArray1, PyArrayDyn, PyReadonlyArray1, PyReadonlyArrayDyn,
    PyReadwriteArray1, PyReadwriteArrayDyn,
};

fn mult(a: f64, mut x: ArrayViewMutD<'_, f64>) {
    x *= a;
}

//#[pyfn(m)]
//#[pyo3(name = "mult")]
#[pyfunction]
fn mult_py(a: f64, mut x: PyReadwriteArrayDyn<f64>) {
    let x = x.as_array_mut();
    mult(a, x);
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn image_kernels(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(mult_py, m)?)?;
    Ok(())
}
