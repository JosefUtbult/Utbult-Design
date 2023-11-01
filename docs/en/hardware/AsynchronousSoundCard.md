---
description: Implementing clock synchronization over USB using data rate matching via asynchronous feedback channels
image: /img/hardware/RustSoundCard/developmentHardware.jpg
---

# Rust sound card

Software security is becoming a more important factor than ever when developing em-
bedded devices. As devices lean more into Internet of Things (IoT) functionality, their
attack surfaces increase. An attacker now has the option to compromise a device re-
motely without ever being in the vicinity of it, as these devices can be reached over the
internet. The need for software validation and in depth testing of embedded devices is
therefore now a must.

One supposed solution for more secure software in embedded devices is the programming
language Rust. This language prioritizes strictly statically typed variables and memory
safety that can be validated during compilation.

The Rust language has come far, but there is still a long way to go in order for it being
a viable option for use in embedded devices. A lot of peripheral application needs to be
implemented and improved for it to be versatile and usable by large.

This project will attempt to tackle one small piece of this puzzle: The Audio
Class functionality of the embedded USB device implementation. The USB protocol
is a widely used for embedded devices to communicate with host computers, such
as personal computers and smartphones. It includes functionality for effectively
streaming audio to and from devices, making it highly suitable for audio cards.

This audio functionality for USB in Rust is already partly implemented, but things such
as clock synchronization and rate feedback matching is currently not supported by the
existing implementations of the USB device driver and the accompanying Audio Class
device implementation. This project will attempt to tackle this by adding this required
functionality and attempting to implement a synchronization strategy for asynchronous
devices called _data rate matching_.

## The USB protocol

The following is a short summary of the relevant parts of the USB protocol.

### Endpoints

![](/img/hardware/RustSoundCard/Endpoints.png){ align=right }

A USB connection consists of a _host_ and a _device_ machine. These are
connected over a single master/single slave bus. Multiple devices can be
connected to a single master via a USB hub device, which extends one bus from
the host into multiple.

A USB device consists on up to 16 endpoints. An endpoint is an address for an
internal function of a USB device, in the same way as a port works in a network.
These 16 endpoints are then separated into an IN and an OUT direction (These
directions are in relation to the host, meaning that an OUT endpoint is for
sending data out from the host into the device). These can be mapped into
different functions to allow different endpoint types. All data on the bus flows
to or from an endpoint. The only endpoint that has a static function is endpoint
zero, which should always configure both its IN and OUT directions as a Control
endpoint.

---

### Frames

The host is in charge of managing data flow on the bus. It does so by scheduling
when a device might transmit. A USB host does this by slicing time into
_frames_. A frame is either 1 ms for Low and Full Speed devices, or 125 μs for
High Speed devices (then called a micro frame).

Each frame starts with the host sending out a Start of Frame (SOF) message to
indicate that a new frame has been started. The host then schedules which
devices should transmit from which endpoints at specific times in the frame.
This allows the host to prioritize specific urgent transmissions, and fill the
rest of the frame with less urgent ones.

![](/img/hardware/RustSoundCard/Frames.png){ align=right }

### Device classes

A USB device can adhere to one or multiple _device classes_. These are classifications of
what function a USB device has, and most USB devices falls into one of these catagories.
These device classes have specifications of their own that the device should adhere to if
it reports itself as a device of the certain class.

One example of a device class is the Audio Class, which encompass audio data formats,
terminal types and MIDI devices. The Audio Class is defined by the _Universal Serial
Bus Device Class Definition for Audio Devices_.

### Descriptors

Descriptors are tables of data, a data structure with well defined formats, that a device
can send to the host using control transfers. These tables are used to describe to the
host the devices attributes and how it can be configured.

There are multiple types of standard descriptors defined by the Universal Serial Bus
Specification. Some of the different descriptors are the Device Descriptor, Endpoint
Descriptors and Configuration Descriptors. All these descriptors has different functions.
The Device Descriptor specifies what device class the device should be configured as,
how much power the device is allowed to draw and if it is able to be but into sleep mode.
The Endpoint Descriptor describes which transfer type should be used by an endpoint
with a certain address and direction and how often this endpoint should be read/written.
An example from the Universal Serial Bus Specification Revision 1.0 of the Endpoint
Descriptor is shown in the following table.

![](/img/hardware/RustSoundCard/EPDescriptor.png)

These are not allowed to be expanded upon by USB class specifications, and
should follow the USB specification for these to be universal across devices of
different device classes. The only exception to this happens to be the USB Audio
Class specification, that has extended the endpoint descriptor, adding two
fields to this descriptor. This revised endpoint descriptor can be seen in the
following table where the fields `bRefresh` and `bSynchAddress` are added to the
bottom.

![](/img/hardware/RustSoundCard/ExtendedEPDescriptor.png)

