# Copyright (C) 2017 RDA Technologies Limited and/or its affiliates("RDA").
# All rights reserved.
#
# This software is supplied "AS IS" without any warranties.
# RDA assumes no responsibility or liability for the use of the software,
# conveys no license or title under any patent, copyright, or mask work
# right to the product. RDA reserves the right to make changes in the
# software without notification.  RDA also make no representation or
# warranty that such application will be suitable for the specified use
# without further testing or modification.

cmake_minimum_required(VERSION 3.4)

project(relayserver)

find_package(Qt4 REQUIRED)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(INSTALL_DIR ${PROJECT_BINARY_DIR}/run)

add_definitions(-DWIN32)
add_definitions(-DUNICODE -D_UNICODE)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /wd4251 /wd4996")
set(CMAKE_C_FLAGS "${CMAKE_CXX_FLAGS} /wd4251 /wd4996")
string(REPLACE "/O2" "/Od /RTC1" CMAKE_C_FLAGS_RELWITHDEBINFO ${CMAKE_C_FLAGS_RELWITHDEBINFO})
string(REPLACE "/O2" "/Od /RTC1" CMAKE_CXX_FLAGS_RELWITHDEBINFO ${CMAKE_CXX_FLAGS_RELWITHDEBINFO})
string(REPLACE "/INCREMENTAL" "/INCREMENTAL:NO" CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO ${CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO})
string(REPLACE "/INCREMENTAL" "/INCREMENTAL:NO" CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO ${CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO})

macro(module_qt_app me)
    QT4_WRAP_CPP(GEN_HEADERS ${HEADERS})
    QT4_WRAP_UI(GEN_FORMS ${FORMS})
    QT4_ADD_RESOURCES(GEN_RESOURCES ${RESOURCES})
    add_executable(${me} ${ARGN} ${SOURCES} ${HEADERS}
        ${GEN_HEADERS} ${GEN_FORMS} ${GEN_RESOURCES}
        ${RC_FILE} ${TRANS})
endmacro()

set(SOURCES main.cpp maindialog.cpp)
set(HEADERS maindialog.h)
set(FORMS maindialog.ui)
set(RESOURCES)

module_qt_app(${PROJECT_NAME} WIN32)
target_link_libraries(${PROJECT_NAME} Qt4::QtCore Qt4::QtGui Qt4::QtNetwork ${PROJECT_SOURCE_DIR}/relaylib/usb_relay_device.lib)

install(PROGRAMS
    ${QT_BINARY_DIR}/QtCored4.dll
    ${QT_BINARY_DIR}/QtGuid4.dll
    ${QT_BINARY_DIR}/QtNetworkd4.dll
    DESTINATION ${INSTALL_DIR}
    CONFIGURATIONS Debug)
install(PROGRAMS
    ${QT_BINARY_DIR}/QtCore4.dll
    ${QT_BINARY_DIR}/QtGui4.dll
    ${QT_BINARY_DIR}/QtNetwork4.dll
    DESTINATION ${INSTALL_DIR}
    CONFIGURATIONS Release RelWithDebInfo)
install(PROGRAMS ${PROJECT_SOURCE_DIR}/relaylib/usb_relay_device.dll DESTINATION ${INSTALL_DIR})
install(TARGETS ${PROJECT_NAME} DESTINATION ${INSTALL_DIR})
