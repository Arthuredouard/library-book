import { useFormik } from 'formik';
import * as Yup from 'yup';

function BookForm() {
  const formik = useFormik({
    initialValues: {
      title: '',
      author: '',
    },
    validationSchema: Yup.object({
      title: Yup.string().required('Required').min(2, 'Too short'),
      author: Yup.string().required('Required'),
    }),
    onSubmit: (values) => {
      fetch('/books', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(values),
      })
        .then(res => res.json())
        .then(data => console.log(data));
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <input
        name="title"
        placeholder="Book Title"
        value={formik.values.title}
        onChange={formik.handleChange}
      />
      {formik.errors.title && <div>{formik.errors.title}</div>}

      <input
        name="author"
        placeholder="Author Name"
        value={formik.values.author}
        onChange={formik.handleChange}
      />
      {formik.errors.author && <div>{formik.errors.author}</div>}

      <button type="submit">Add Book</button>
    </form>
  );
}

export default BookForm;
