<?php

/*///////////////////////////////////////////////////////////////
// Archivo: lib_facturacion_electronica.inc
// Fecha: 2007/07/12
// Descripcion:
///////////////////////////////////////////////////////////////*/

	include_once "librerias/lib_ini.inc";
	include_once "librerias/lib_db.inc";
	include_once "librerias/lib_configuracion.inc";
	include_once "librerias/lib_general.inc";
	include_once "librerias/formulario.inc";
	include_once "librerias/operaciones.inc";
	include_once "librerias/lib_privadas.inc";
	include_once "librerias/JSON.php";
  
 

/*///////////////////////////////////////////////////////////////
// Funcion captura($accion,$estado,$id,$mensaje,$formulario)
// Fecha: 2007/07/12
// Descripcion:
///////////////////////////////////////////////////////////////*/
function captura($accion,$estado,$id,&$arreglo_mensaje,&$formulario,&$arreglo_datos)
{
	$error_preliminar=retornar_errores_preliminales($arreglo_mensaje);
	$error_datos=retornar_datos($accion,$id,$arreglo_datos);
	$res_consistencia=validar_consistencia_datos($accion,$estado,$arreglo_mensaje);
	$res_proceso=validar_procesos($accion,$estado,$id,$arreglo_mensaje,$formulario);
	$formulario=visualizacion_formulario($accion,$estado,$arreglo_datos);
	return TRUE;
}

/*///////////////////////////////////////////////////////////////
// Funcion retornar_errores_preliminales()
// Fecha: 2007/07/12
// Descripcion: 
///////////////////////////////////////////////////////////////*/
function retornar_errores_preliminales(&$arreglo_mensaje)
{		 
  global $accion,$estado,$seleccionar,$tipo_mensaje,$bandera_error;   
  if($accion=="ingresar" && $estado==1){
    $contar_seleccionado=0;
    $fecha_actual=fecha_hora_actual();
    $bandera_error=FALSE;
   if(($seleccionar!=FALSE) && is_array($seleccionar) && count($seleccionar)>0){
     while((list($id_transaccion, $val)=each($seleccionar))){ 
       if($val=="1" AND $bandera_error==FALSE){
       
          $arreglo_asiento=array();
          $contar_seleccionado++;
          if($bandera_error==FALSE){
            $data=genera_factura_compartida_electronica($id_transaccion,$codigo_cia,$tipo_documento,$numero_documento);
              if($data=="F"){
                $arreglo_mensaje[]="Error de conexi&oacuten";
                $bandera_error=TRUE;
              }if($data=="S"){
                $arreglo_mensaje[]="No se le puede generar factura electronica para este documento";
                $bandera_error=TRUE;
              }elseif($data=="V"){
                //$arreglo_mensaje[]="$data";
              }else{
                $arreglo_mensaje[]="$data";
                $bandera_error=TRUE;
              }
            }
          }                
        }
      }else{
        $arreglo_mensaje[]="No hay datos";
        $estado=0;
      }  
      if($contar_seleccionado==0){
          $arreglo_mensaje[]="No selecciono ningun registro";
           $estado=0;
      }else{
           if($bandera_error==FALSE) 
          $arreglo_mensaje[]="Facturado electronicamente con exito";
          else
           $arreglo_mensaje[]="<BR>No esta bien configurado la transaccion $codigo_cia-$tipo_documento-$numero_documento ICAS o transaccion ya fue facturada electronicamente";
      }
  }
  return TRUE;
}

/*///////////////////////////////////////////////////////////////
// Funcion retornar_datos($accion,$id,$arreglo_errores,&$arreglo_datos)
// Fecha: 2007/07/12

// Descripcion: 
///////////////////////////////////////////////////////////////*/
function retornar_datos($accion,$id,&$arreglo_datos)
{
	return TRUE;
}

/*///////////////////////////////////////////////////////////////
// Funcion visualizacion_formulario($arreglo_datos,$error_preliminar,$error_datos,$accion,$estado)
// Fecha: 2007/07/12

// Descripcion: 
///////////////////////////////////////////////////////////////*/
function visualizacion_formulario($accion,$estado,$arreglo_datos)
{
        global $ruta_imagen,$codigo_cia_empresa,$estado_registro,$facturar_electronicamente,$arreglo_mensaje,$codigo_un,$seleccionar,$seleccionar_todos,$fecha_inicial,$fecha_final,$codigo_cia,$id,$url_servidor,$primero,$evento_consulta,$cadena,$filtrar;

	if(($accion=="ingresar" || $accion=="actualizar") && ($estado==0 OR $estado==1)){
				
    $cantidad_registro_procesar=100;
    if($facturar_electronicamente==0){
      $seleccionar=array();
      $seleccionar_todos="";
    }
    $arreglo_empresas=retornar_empresas();
    $arreglo_empresas_aux=$arreglo_empresas;
    if(strlen($codigo_cia_empresa)==0){
      if(is_array($arreglo_empresas))
       list($codigo_cia_empresa,$codigo_cia_empresaaux)=each($arreglo_empresas);
    }
    
    $selempresas=crearselectorevento(codigo_cia_empresa,$codigo_cia_empresa,$arreglo_empresas_aux,true,"  onchange=\"ir_insertar_actualizar('$url_servidor/privado/facturacion_compartida_electronica.php?accion=ingresar&estado=0&facturar_electronicamente=0',1,1);\"","");
    $resul_cia=retornar_dato_empresa('',$codigo_cia_empresa);
    $factura_electronica=$resul_cia["factura_electronica"];
    
    $entorno=panel_cuadro_superior("Facturar Electronicamante DIAN","Facturar Electronicamante DIAN","tablacabecera","tablacontenido");
		if (strlen($primero)==0){
			$primero=0;
			$cadena="";
			$filtrar=4;
		}elseif ($evento_consulta==1){
			$primero-=($cantidad_registro_procesar);
		}else if ($evento_consulta==2){
			$primero+=($cantidad_registro_procesar);
		}else if ($evento_consulta==3){
			$primero=$primero;
		}else{
			$primero=0;
		}
   $ultimo = $cantidad_registro_procesar + 1;	    
  	
      switch($filtrar){
  		case "1" :
  			if (strlen($cadena)> 0)
  				$query_filtrar=" AND F420031_codigo_cia LIKE '$cadena%'";
  			else
  				$query_filtrar=" AND F420031_codigo_cia=''";
  			break;
  		case "2" : 
  			if (strlen($cadena)> 0)
  				$query_filtrar=" AND F420031_tipo_documento LIKE '%$cadena%'";
  			else
  				$query_filtrar=" AND F420031_tipo_documento = ''";
  			break;
  		case "3" : 
  			if (strlen($cadena)> 0)
  				$query_filtrar=" AND F420031_numero_documento LIKE '%$cadena%'";
  			else
  				$query_filtrar=" AND F420031_numero_documento = ''";
  			break;
    	default  : 
  				$query_filtrar="";
  			break;
  		}
    	
      if ($fecha_inicial && $fecha_final && verificar_fecha($fecha_inicial) && verificar_fecha($fecha_final)){
        $where_fecha_ini=" AND (F420031_fecha_venta>='$fecha_inicial' and F420031_fecha_venta<='$fecha_final')";
      }elseif ($fecha_inicial && verificar_fecha($fecha_inicial)){
      	$where_fecha_ini=" AND F420031_fecha_venta >= '$fecha_inicial'";
      }elseif ($fecha_final && verificar_fecha($fecha_final)){
      	$where_fecha_fin=" AND  F420031_fecha_venta <= '$fecha_final'";
      }else{
      	$where_fecha_fin="";
      	$where_fecha_ini="";
      }
		  $where_fecha=" $where_fecha_ini $where_fecha_fin";
    
    if($factura_electronica=='S'){
      $query=<<<QUERY
    	 select F420031_id_factura as id,F420031_codigo_cia as codigo_cia,F420031_fecha_venta as fecha,
      F420031_tipo_documento as  tipo_documento,
      F420031_numero_documento as numero_documento,F420031_codigo_un as codigo_un, 	F420031_cliente as tercero, 
      F420031_total_pagar as total 
      from F420031_facturas_compartida,F420032_transfacturas_compartida
      WHERE 	F420031_id_factura=F420032_id_factura AND F420031_estado='Facturado' AND F420031_contabilizado='P' 
      AND F420031_codigo_cia='$codigo_cia_empresa' 
      AND F420032_tipo='Productos' 
      $query_filtrar
      $where_fecha
      group by F420031_id_factura
      ORDER BY F420031_codigo_cia,F420031_fecha_venta DESC
  LIMIT $ultimo OFFSET $primero
QUERY;


	$resultado_cuenta=consultar($query);
	$total_items = count($resultado_cuenta);
}

	$arreglo_filtrar=array("1"=>"Compañia","2"=>"Tipo Documento","3"=>"Documento","4"=>"Todos");
	$sel_filtrar=crearselector(filtrar,$filtrar,$arreglo_filtrar,TRUE,"");

  	$entorno_fecha=<<<ENTORNO
   <tr>
           <td  align="right" class="referencia">Fecha&nbsp;inicial:&nbsp;</td>
           <td >
                      <input type="text" class="deftxtfield" name="fecha_inicial" size="10" maxlength="10" value="$fecha_inicial">&nbsp;<img src="$ruta_imagen/calendario.gif" alt="Mostrar Calendario" title="Mostrar Calendario" align="absmiddle" border="0" height="20" width="20" onclick="displayCalendar(document.formulario.fecha_inicial,'yyyy-mm-dd',this,false,'','$ruta_imagen/');">
              </td>
             <td colspan="2" align="left" class="referencia">Fecha&nbsp;final:&nbsp;
                        <input type="text" class="deftxtfield" name="fecha_final" size="10" maxlength="10" value="$fecha_final">&nbsp;<img src="$ruta_imagen/calendario.gif" alt="Mostrar Calendario" title="Mostrar Calendario" align="absmiddle" border="0" height="20" width="20" onclick="displayCalendar(document.formulario.fecha_final,'yyyy-mm-dd',this,false,'','$ruta_imagen/');">
              </td>
              </tr>
ENTORNO;
   
         $selecttxt_todos="";
         if($seleccionar_todos=="1"){
           $selecttxt_todos="checked";
         }
                                  
		$entorno.=<<<ENTORNO
		<input type="hidden" name="primero" value="$primero">
		                    <table  align="center" border="0" cellpadding="0" cellspacing="0" width="98%">
                        <tr>
                          <td height="10" width="45%">&nbsp;</td>
                          <td align="right" width="65%">&nbsp;</td>
                        </tr>
                        <tr>
                          <td class="cuestionario" colspan="2">
                         
                          &nbsp;
                      <table width="567" border="0" cellspacing="0" cellpadding="0">
                         <tr> 
			<td width="100" align="right" class="referencia">Compa&ntilde;ia:&nbsp;</td>
                        <td colspan="3" width="467"> 
                          <table width="467" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100"> 
     		$selempresas
                              </td>
                              <td width="367"> 
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      <tr> 
			<td width="100" align="right" class="referencia">Filtrar&nbsp;Por:&nbsp;</td>
                        <td colspan="3" width="467"> 
                          <table width="467" border="0" cellspacing="0" cellpadding="0">
                            <tr> 
                              <td width="100"> 
     		$sel_filtrar
                              </td>
                              <td width="367"> 
                                <input type="text" class="deftxtfield" name="cadena" size="30" value="$cadena">
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                      $entorno_fecha
                    </table>  
                    
                      <table border="0" cellspacing="0" cellpadding="0">
                      <tr> 
                          <td width="530" class="cuestionario">&nbsp;</td>
                        <td width="120">      <input type="submit" class="defbottonlogin" name="mostrar" value="Mostrar" onclick="ir_insertar_actualizar('$url_servidor/privado/facturacion_compartida_electronica.php?accion=ingresar&estado=0&facturar_electronicamente=0',1,1);"></td>
                        <td width="120" align="left"> 
                         <input type="submit" class="defbottonlogin" name="Facturar Electronicamente" value="Facturar Electronicamente" onclick="ir_insertar_actualizar('$url_servidor/privado/facturacion_compartida_electronica.php?accion=ingresar&estado=1&facturar_electronicamente=1',1,1);">
                        </td>
                      </tr>
                       </table> 
                                               
                          </td>
                        </tr>
                        <tr>
                          <td class="cuestionario">&nbsp;</td>
                          <td class="cuestionario">&nbsp;</td>
                        </tr>
                        <tr>
                          <td colspan="2 "class="cuestionario">
                          <div >
                          <table width="100%" border="0" cellpadding="1" cellspacing="1">
                        <tr> 
            		   <td width="1%" align="center" class="encabezadocon"><input type="checkbox" name="seleccionar_todos"  $selecttxt_todos onclick="ir_insertar_actualizar('$url_servidor/privado/facturacion_compartida_electronica.php?evento_consulta=3&primero=$primero&accion=ingresar&estado=0&facturar_electronicamente=1&estado_registro=1',1,1);" value="1"></td>
                    <td width="30%" align="center" class="encabezadocon">Compañia</td>
                  <td width="7%" align="center" class="encabezadocon">Fecha</td>
                  <td width="5%" align="center" class="encabezadocon">Tipo</td>
            		  <td width="7%" align="center" class="encabezadocon">N.documento</td>
            		  <td width="10%" align="center" class="encabezadocon">U.Negocio</td>
            		  <td width="30%" align="center"class="encabezadocon">Tercero/Nota</td>
                   <td width="10%" align="center"class="encabezadocon">Total</td>
            		  </tr>
ENTORNO;
                        
    $icolor=0;
    $cont=0; 
    $array_temp=array();
    $arreglo_tipo_documentos=retornar_documentos("");
    $valor_total=0;
    while (is_array($resultado_cuenta) && (list($key,$registro)=each($resultado_cuenta)) && ($cont < $ultimo - 1)){
    if ($icolor%2==0)
			$estilo="contenidocon";
		else
			$estilo="contenidocon1";
		
    $icolor++;
		$cont++;
    $id=$registro["id"];
		$tipo_documento=$registro["tipo_documento"];
		$numero_documento=$registro["numero_documento"];
    $codigo_cia=$registro["codigo_cia"];
   	$codigo_ciatxt=$arreglo_empresas[$codigo_cia];
    $fecha=$registro["fecha"];
    $codigo_un=$registro["codigo_un"];
    $tercero=$registro["tercero"];
		$total=$registro["total"];
    $array_temp[$id] = $id; 
   
   $selecttxt="";
   if($seleccionar_todos=="1"){
     $selecttxt="checked";
   }else{
      if($seleccionar[$id]=="1" && $estado_registro!="1")
           $selecttxt="checked";
   } 
    $valor_total+=$total;
      
    $total=formatear_numero($total);
    
    
        
		$entorno.=<<<ENTORNO
        <tr id="fila$cont" class="$estilo" onmouseover="cambiar_color($cont, '$estilo', 'contenidoresaltado', 'contenidoseleccionado', '1')" onmouseout="cambiar_color($cont, '$estilo', 'contenidoresaltado', 'contenidoseleccionado', '2')" onmousedown="cambiar_color($cont, '$estilo', 'contenidoresaltado', 'contenidoseleccionado', '3')">
        <td valign="top" align="center"><input type="checkbox" $selecttxt name="seleccionar[$id]"  value="1"  onclick="no_chequear_todos(document.formulario.seleccionar_todos);"></td>
        <td valign="top" align="left">$codigo_ciatxt</td>
        <td>$fecha</td>
        <td>$tipo_documento</td>
        <td>$numero_documento</td>
        <td>$codigo_un</td>
        <td  valign="top" >$tercero</td>
        <td  valign="top" align="right" >$total</td>
        </tr>
ENTORNO;

	}  
  
  
  if(is_array($seleccionar)){
    while((list($key, $val)=each($seleccionar))){                                             
        if(!in_array($key,$array_temp)){
         $entorno.=<<<ENTORNO
          <input type="hidden" name="seleccionar[$key]" id="seleccionar[$key]" value="$val">
ENTORNO;
				}            
	   }
   }    
    if($primero>0){
		$boton_anterior = <<<BOTONANTERIOR
		<input type="button" class="defbottonlogin" value="<" name="anteriores" alt="Anteriores" title="Anteriores" align="middle" onclick="ir_insertar_actualizar('$url_servidor/privado/facturacion_compartida_electronica.php?accion=ingresar&estado=0&evento_consulta=1&facturar_electronicamente=1',1,1);">
BOTONANTERIOR;
		}      	
		if ($total_items > $cantidad_registro_procesar){
  	  $boton_siguiente =<<<BOTONSIGUIENTE
      <input type="button"  class="defbottonlogin" value=">" name="siguientes" alt="Siguientes" title="Siguientes" align="middle" onclick="ir_insertar_actualizar('$url_servidor/privado/facturacion_compartida_electronica.php?accion=ingresar&estado=0&evento_consulta=2&&facturar_electronicamente=1',1,1);">
BOTONSIGUIENTE;
	  }
     
     
     $valor_total=formatear_numero($valor_total);
                         
                          $entorno.=<<<ENTORNO
      <tr  >
     <td valign="top" align="left"&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
	   <td>&nbsp;</td>
      <td align="right"></td>
      <td >&nbsp;</td>
      <td  valign="top" >&nbsp;</td>
      <td align="right"><b>$valor_total</b></td>
      </tr>
                        	</table>
                        	</div>
                        	</td>
                        <tr>
                          <td class="cuestionario">&nbsp;</td>
                          <td class="cuestionario">&nbsp;</td>
                        </tr>
                        <tr>
                          <td class="cuestionario" align="right">&nbsp;$boton_anterior</td>
                          <td class="cuestionario" >$boton_siguiente</td>
                        </tr>
                        <tr>
                          <td class="cuestionario">&nbsp;</td>
                          <td class="cuestionario">&nbsp;</td>
                        </tr>
                      </table>
                       <table  align="center" border="0" cellpadding="0" cellspacing="0" width="98%">
                        <tr>
                          <td class="cuestionario" align="right" width="35%">&nbsp;</td>
                          <td class="cuestionario" width="45%">&nbsp; </td>
                          <td class="cuestionario" width="20%">$boton </td>
                        </tr>
                       </table>                    
ENTORNO;
	  $entorno.=panel_cuadro_inferior("tablapie");
    $html=$entorno;
	}else{
		$html="";
	}
	return $html;
}

/*///////////////////////////////////////////////////////////////
// Funcion procesarbd($accion,$estado,$id,$arreglo_mensaje,$formulario)
// Fecha: 2004/03/20
// Descripcion: 
///////////////////////////////////////////////////////////////*/
function procesarbd($accion,$estado,&$id,&$arreglo_datos,&$arreglo_mensaje,&$formulario)
{
   global $bandera_error,$tipo_mensaje;
   
  // if((count($arreglo_mensaje)==1 && $tipo_mensaje==TRUE) || (count($arreglo_mensaje)<1 && $tipo_mensaje==FALSE)){
  
   if(count($arreglo_mensaje)>0){
     if($accion=='ingresar' && $estado==1){
        if($bandera_error==TRUE){
           return FALSE;
        }else{
           return TRUE;
        }
       }
    }
 
}

/*///////////////////////////////////////////////////////////////
// Funcin validar_consistencia_datos($accion,$estado,$arreglo_mensaje)
// Fecha: 2007/06/27
// Descripcion: 
///////////////////////////////////////////////////////////////*/
function validar_consistencia_datos($accion,$estado,&$arreglo_mensaje)
{
 return  TRUE;
}




function validar_procesos($accion,$estado,$id,&$arreglo_mensaje,$formulario)
{
     return  TRUE;
}


function mostrar($accion,$estado,$arreglo_datos,&$arreglo_mensaje,&$formulario_mostrar,$res_procesarbd)
{
	  return TRUE;
}

?>