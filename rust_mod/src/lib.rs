use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}


#[pyfunction]
fn get_fibonacci(number: isize) -> PyResult<u128> {
    if number == 0 {
        return Ok(0);
    }
    let mut n_0: u128= 0;
    let mut n_1: u128 = 1;
    let mut tmp: u128;
    for _ in 0..(number-1) {
        tmp = n_1;
        n_1 = n_1+n_0;
        n_0 = tmp;
    }
    Ok(n_1)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_mod(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(get_fibonacci, m)?)?;
    Ok(())
}