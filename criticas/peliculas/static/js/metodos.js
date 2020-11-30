function Validar() {
	nom = document.getElementById('Nombre').value;
	ap = document.getElementById('Apellido').value;
	con = document.getElementById('Contraseña1').value;
	con2 = document.getElementById('Contraseña2').value;
	edad = document.getElementById('Edad').value;
	gen1 = document.getElementById('Checkbox1');
	gen2 = document.getElementById('Checkbox2');
	nac = document.getElementById('Opciones').selectedIndex;

	if (nom.length <= 2 || (/^\s{1,100}$/).test(nom) || (/^\W{1,100}$/).test(nom) || (/^\d{1,100}$/).test(nom))
	{
		if ((/^\W{1,100}$/).test(nom) || (/^\d{1,100}$/).test(nom))
		{
			alert('Debe ingresar letras en el nombre');
			document.getElementById('Nombre').value="";
			document.getElementById('Nombre').focus();
		}
		else
		{
			alert('Error... debe ingresar un nombre con mas de dos caracteres');
			document.getElementById('Nombre').value="";
			document.getElementById('Nombre').focus();
		}
	}

	else if(ap.length <= 2 || (/^\s{1,100}$/).test(ap) || (/^\W{1,100}$/).test(ap) || (/^\d{1,100}$/).test(ap))
	{
		if ((/^\W{1,100}$/).test(ap) || (/^\d{1,100}$/).test(ap))
		{
			alert('Debe ingresar letras en el apellido');
			document.getElementById('Apellido').value="";
			document.getElementById('Apellido').focus();
		}
		else
		{
			alert('Error... debe ingresar un apellido con mas de dos caracteres');
			document.getElementById('Apellido').value="";
			document.getElementById('Apellido').focus();
		}
	}

	else if(!(/^\d{1,2}$/).test(edad))
	{
		if ((/^\s{1,100}$/).test(edad) || (/^\D{1,100}$/).test(edad))
		{
			alert('Error... debe ingresar una edad con numeros');
			document.getElementById('Edad').value="";
			document.getElementById('Edad').focus();

		}
		else if(edad.length == 0)
		{
			alert('Error... debe ingresar una edad');
			document.getElementById('Edad').value="";
			document.getElementById('Edad').focus();
		}
		else
		{
			alert('Error... debe ingresar una edad de hasta 2 digitos');
			document.getElementById('Edad').value="";
			document.getElementById('Edad').focus();
		}
	}

	else if(!gen1.checked && !gen2.checked)
	{
		alert('Error... debe seleccionar un genero');
	}

	else if(nac == null || nac == 0)
	{
		alert('Error... debe elegir un pais de origen');
	}

	else if(con.length <= 5 || (/^\s{1,100}$/).test(con))
	{
		alert('Error... debe ingresar una contraseña con al menos 6 caracteres');
		document.getElementById('Contraseña1').value="";
		document.getElementById('Contraseña1').focus();
	}

	else if(con2 != con)
	{
		alert('Error... debe ingresar la misma contraseña');
		document.getElementById('Contraseña2').value="";
		document.getElementById('Contraseña2').focus();
	}

	else
	{
		alert('Se ha registrado exitosamente');
		document.getElementById('Nombre').value="";
		document.getElementById('Apellido').value="";
		document.getElementById('Edad').value="";
		document.getElementById('Contraseña1').value="";
		document.getElementById('Contraseña2').value="";
	}
}



