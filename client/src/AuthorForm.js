// client/src/AuthorForm.js
import { useFormik } from 'formik';
import * as Yup from 'yup';

function AuthorForm({ onAuthorAdded }) {
  const formik = useFormik({
    initialValues: { name: '' },
    validationSchema: Yup.object({
      name: Yup.string()
        .required('Le nom est requis')
        .min(2, 'Nom trop court'),
    }),
    onSubmit: (values, { resetForm }) => {
      fetch('/authors', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(values),
      })
        .then(res => res.json())
        .then(data => {
          if (onAuthorAdded) onAuthorAdded(data);
          resetForm();
        })
        .catch(err => {
          console.error('Erreur lors de l’ajout de l’auteur:', err);
        });
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <h3>Ajouter un auteur</h3>
      <input
        name="name"
        placeholder="Nom de l’auteur"
        value={formik.values.name}
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
      />
      {formik.touched.name && formik.errors.name && (
        <div style={{ color: 'salmon' }}>{formik.errors.name}</div>
      )}
      <button type="submit">Ajouter</button>
    </form>
  );
}

export default AuthorForm;

