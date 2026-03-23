# Contributing Guide

## Table of Contents

<!--toc:start-->
- [Contributing Guide](#contributing-guide)
  - [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
- [Introduction](#introduction)
- [Schema](#schema)
- [Expressions](#expressions)
- [Testing](#testing)
- [Packages](#packages)
  - [The anatomy of a package](#the-anatomy-of-a-package)
  - [Package specification](#package-specification)
    - [`name`](#name)
    - [`description`](#description)
    - [`homepage`](#homepage)
    - [`licenses`](#licenses)
    - [`languages`](#languages)
    - [`categories`](#categories)
    - [`deprecation`](#deprecation)
    - [`source`](#source)
    - [`bin`](#bin)
    - [`share`](#share)
    - [`opt`](#opt)
- [Language Servers](#language-servers)
  - [The anatomy of a language server](#the-anatomy-of-a-language-server)
  - [Language Server specification](#language-server-specification)
<!--toc:end-->

> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT
> RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14][bcp14],
> [RFC2119][rfc2119], and [RFC8174][rfc8174] when, and only when, they appear in all capitals, as shown here.

# Requirements

At least one of the following conditions MUST be fulfilled for new tools to be added to the registry.

1. At least 100 stars on GitHub.
1. The tool is officially recommended by a reputable consortium, foundation, or company.

Even if one, or all, of the previous conditions are fulfilled, new package additions may be rejected for other 
reasons.

# Introduction

- Make sure to follow the [naming guidelines](#name).
- Refer to the [common fields example](#common-fields) for a good starting point for a new package.
- Refer to the different [examples](#examples) and/or existing package definitions for further guidance.
- Testing a package MUST be done locally prior to creating a PR. See [testing](#testing) for more information.
