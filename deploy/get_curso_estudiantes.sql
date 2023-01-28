create or replace function public.get_curso_estudiantes(
	turno_pk integer,
	gestion integer,
	curso_pk integer
) returns json as
$$
/**
 * Function: get_curso_estudiantes
 * Author: Luis F. Flores C.
 * Descripcion: Retorna el listado de todos los estudiantes que pertenecen aun curso en especifico
 *              por turno y gestion.
 */
declare
	response json;
begin
	response := (
		select array_to_json(array_agg(estudiantes))
		from (
			select
				cc.denominacion,
				cc.paralelo,
				pn.nivel,
				pt.turno,
				ii.gestion,
				pe.rude,
				pe.nombre,
				pe.apellido_paterno,
				pe.apellido_materno,
				pe.documento,
				pd.sigla,
				pe.fotografia,
				pe.celular,
				pg.genero
			from curso_curso cc inner join
			     parametro_nivel pn on (cc.nivel_id=pn.id) inner join
			     parametro_turno pt on (cc.turno_id=pt.id) inner join
			     inscripcion_inscripcion ii on (cc.id=ii.curso_id and ii.fecha_eliminacion is null ) inner join
			     persona_estudiante pe on (ii.estudiante_id=pe.id and pe.fecha_eliminacion is null) inner join
			     parametro_tipoestudiante pte on (ii.tipoestudiante_id=pte.id) inner join
			     parametro_departamento pd on (pe.expedido_id=pd.id) inner join
			     parametro_genero pg on (pe.genero_id=pg.id)
			where cc.id = $3 and ii.gestion = $2 and pt.id = $1 and cc.fecha_eliminacion is null
		) as estudiantes
	);

	if response is null then
		response := json_build_array();
	end if;

	return response;
end;

$$
language plpgsql;
