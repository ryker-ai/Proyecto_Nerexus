Proyecto Nerexus

Proyecto desarrollado como Trabajo de Fin de Ciclo de Sistemas Microinformáticos y Redes (SMR).

Nerexus consiste en el diseño, implementación y validación de una infraestructura tecnológica corporativa completa para una empresa de inversión inmobiliaria, desplegada íntegramente sobre un entorno virtualizado VMware Workstation Pro.

La arquitectura ha sido diseñada siguiendo principios de segmentación de red y seguridad perimetral, incorporando servicios empresariales esenciales, monitorización continua y una plataforma web corporativa.

Objetivos del proyecto
Diseñar una infraestructura corporativa escalable y segura.
Implementar segmentación de red mediante zonas de seguridad.
Desplegar servicios corporativos esenciales.
Aplicar medidas de seguridad perimetral.
Validar el funcionamiento mediante pruebas técnicas.
Documentar todo el proceso de implementación.
Tecnologías utilizadas
VMware Workstation Pro
Palo Alto Networks NGFW
Cisco CSR1000V
Ubuntu Server 24.04 LTS
Apache2
Bind9 DNS
ISC DHCP Server
OpenLDAP
Squid Proxy
Nagios Core
Python 3
HTML5 & CSS3
Wireshark
Nmap
Draw.io
Arquitectura

La infraestructura está segmentada en cuatro zonas de seguridad:

Zona Externa (WAN)
DMZ Externa
DMZ Interna
Red Corporativa (Inside)

Esta segmentación permite aislar servicios críticos, reducir la superficie de ataque y aplicar políticas de control de tráfico mediante un firewall Palo Alto NGFW.

Servicios implementados
DMZ Externa
Servidor Web Apache2
Servidor DNS Bind9
Proxy Squid
DMZ Interna
OpenLDAP
ISC DHCP Server
Nagios Core
Seguridad
Palo Alto NGFW
NAT
IDS/IPS
Control de tráfico entre zonas
Principios Zero Trust
Funcionalidades destacadas
Segmentación avanzada de red
Resolución DNS interna y externa
Asignación dinámica de direcciones IP
Directorio centralizado de usuarios
Proxy corporativo con registro de actividad
Monitorización de servicios en tiempo real
Plataforma web corporativa
Generador de contraseñas seguras desarrollado en Python
Capturas y documentación

En este repositorio se incluyen:

Diagramas de red
Capturas de configuración
Evidencias de validación
Scripts desarrollados
Documentación técnica completa

Ivan Martin Castañares,
Rafael Lozano Rubio

https://github.com/ryker-ai/PROYETO-NEREXUS.git

Proyecto desarrollado por los alumnos del ciclo de Sistemas Microinformáticos y Redes (SMR) como Trabajo de Fin de Ciclo 2025-2026.
