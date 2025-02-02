schame  = {
    "type" : "object",
    "properties": {
        "data" : {
            "type": "object",
            "properties": {
                "@type" : {"$ref" : "#/definitions/@type"},
                "element" : {"$ref" : "#/definitions/element"},
                "value" : {"$ref" : "#/definitions/value"}
            }
            
        },
        "datacontenttype": {
            "type" : "string",
            "enum": ["application/json"]
        },
        "id" : {
            "type": "string"
        },
        "source" : {"$ref": "#/definitions/UrlType"},
        "specversion": {
            "type": "string"
        },
        "subject" :{
            "type" : "string",
            "enum": ["ASSET_ADMINISTRATION_SHELL"]
        },
        "time" : {
            "type": "string"
        }
        
    },
    "definitions": {
        "@type": {
            "type": "string"

        },
        "element" :{
            "type" : "object",
            "properties": {
                "keys" : {"$ref": "#/definitions/Keys"},
                "type" : {"$ref": "#/definitions/ReferenceTypes"}
            }
        }, 
        "Keys": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Key"
                    },
                    "minItems": 1
                },
        "Key": {
            "type": "object",
            "properties": {
                "type": {
                    "$ref": "#/definitions/KeyTypes"
                },
                "value": {
                    "$ref": "#/definitions/UrlType"
                }
            },
            "required": ["type", "value"]
        },
        "KeyTypes": {
            "type": "string",
            "enum": [
                "AnnotatedRelationshipElement",
                "AssetAdministrationShell",
                "BasicEventElement",
                "Blob",
                "Capability",
                "ConceptDescription",
                "DataElement",
                "Entity",
                "EventElement",
                "File",
                "FragmentReference",
                "GlobalReference",
                "Identifiable",
                "MultiLanguageProperty",
                "Operation",
                "Property",
                "Range",
                "Referable",
                "ReferenceElement",
                "RelationshipElement",
                "Submodel",
                "SubmodelElement",
                "SubmodelElementCollection",
                "SubmodelElementList"
            ]
        }, 
        "ModelType": {
            "type": "string",
            "enum": [
                "AnnotatedRelationshipElement",
                "AssetAdministrationShell",
                "BasicEventElement",
                "Blob",
                "Capability",
                "ConceptDescription",
                "DataSpecificationIec61360",
                "Entity",
                "File",
                "MultiLanguageProperty",
                "Operation",
                "Property",
                "Range",
                "ReferenceElement",
                "RelationshipElement",
                "Submodel",
                "SubmodelElementCollection",
                "SubmodelElementList"
            ]
        },
        "UrlType" : {
            "type": "string",
                    "minLength": 1,
                    "maxLength": 2000,
                    "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
        },
        "AssetInformation" :{
            "type" : "object",
            "properties": {
                "assetKind" : {
                    "type" : "string"
                },
                "assetType": {
                    "type" : "string",
                    "enum": ["Instance", "Type"]
                },
                "globalAssetId": {
                    "$ref": "#/definitions/UrlType"
                }
            }

        },
        "ReferenceTypes": {
            "type": "string",
            "enum": ["ExternalReference", "ModelReference"]
        },
        "AasSubmodelElements": {
            "type": "string",
            "enum": [
                "AnnotatedRelationshipElement",
                "BasicEventElement",
                "Blob",
                "Capability",
                "DataElement",
                "Entity",
                "EventElement",
                "File",
                "MultiLanguageProperty",
                "Operation",
                "Property",
                "Range",
                "ReferenceElement",
                "RelationshipElement",
                "SubmodelElement",
                "SubmodelElementCollection",
                "SubmodelElementList"
            ]
        },
        "AbstractLangString": {
            "type": "object",
            "properties": {
                "language": {
                    "type": "string",
                    "pattern": "^(([a-zA-Z]{2,3}(-[a-zA-Z]{3}(-[a-zA-Z]{3}){2})?|[a-zA-Z]{4}|[a-zA-Z]{5,8})(-[a-zA-Z]{4})?(-([a-zA-Z]{2}|[0-9]{3}))?(-(([a-zA-Z0-9]){5,8}|[0-9]([a-zA-Z0-9]){3}))*(-[0-9A-WY-Za-wy-z](-([a-zA-Z0-9]){2,8})+)*(-[xX](-([a-zA-Z0-9]){1,8})+)?|[xX](-([a-zA-Z0-9]){1,8})+|((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)))$"
                },
                "text": {
                    "type": "string",
                    "minLength": 1,
                    "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                }
            },
            "required": ["language", "text"]
        },
        "AdministrativeInformation": {
            "allOf": [
                {
                    "$ref": "#/definitions/HasDataSpecification"
                },
                {
                    "properties": {
                        "version": {
                            "type": "string",
                            "allOf": [
                                {
                                    "minLength": 1,
                                    "maxLength": 4
                                },
                                {
                                    "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                                },
                                {
                                    "pattern": "^(0|[1-9][0-9]*)$"
                                }
                            ]
                        },
                        "revision": {
                            "type": "string",
                            "allOf": [
                                {
                                    "minLength": 1,
                                    "maxLength": 4
                                },
                                {
                                    "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                                },
                                {
                                    "pattern": "^(0|[1-9][0-9]*)$"
                                }
                            ]
                        },
                        "creator": {
                            "$ref": "#/definitions/Reference"
                        },
                        "templateId": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 2000,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        }
                    }
                }
            ]
        },
        "DataElement": {
            "$ref": "#/definitions/SubmodelElement"
        },
        "DataElement_choice": {
            "oneOf": [
                {
                    "$ref": "#/definitions/File"
                },
                {
                    "$ref": "#/definitions/Property"
                },
                {
                    "$ref": "#/definitions/Range"
                },
                {
                    "$ref": "#/definitions/ReferenceElement"
                }
            ]
        },
        "DataSpecificationContent": {
            "type": "object",
            "properties": {
                "modelType": {
                    "$ref": "#/definitions/ModelType"
                }
            },
            "required": ["modelType"]
        },
        "DataSpecificationContent_choice": {
            "oneOf": [
                {
                    "$ref": "#/definitions/DataSpecificationIec61360"
                }
            ]
        },
        "DataSpecificationIec61360": {
            "allOf": [
                {
                    "$ref": "#/definitions/DataSpecificationContent"
                },
                {
                    "properties": {
                        "preferredName": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/LangStringPreferredNameTypeIec61360"
                            },
                            "minItems": 1
                        },
                        "shortName": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/LangStringShortNameTypeIec61360"
                            },
                            "minItems": 1
                        },
                        "unit": {
                            "type": "string",
                            "minLength": 1,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        "unitId": {
                            "$ref": "#/definitions/Reference"
                        },
                        "sourceOfDefinition": {
                            "type": "string",
                            "minLength": 1,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        "symbol": {
                            "type": "string",
                            "minLength": 1,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        "dataType": {
                            "$ref": "#/definitions/DataTypeIec61360"
                        },
                        "definition": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/LangStringDefinitionTypeIec61360"
                            },
                            "minItems": 1
                        },
                        "valueFormat": {
                            "type": "string",
                            "minLength": 1,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        "valueList": {
                            "$ref": "#/definitions/ValueList"
                        },
                        "value": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 2000,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        "levelType": {
                            "$ref": "#/definitions/LevelType"
                        },
                        "modelType": {
                            "const": "DataSpecificationIec61360"
                        }
                    },
                    "required": ["preferredName"]
                }
            ]
        },
        "DataTypeDefXsd": {
            "type": "string",
            "enum": [
                "xs:anyURI",
                "xs:base64Binary",
                "xs:boolean",
                "xs:byte",
                "xs:date",
                "xs:dateTime",
                "xs:decimal",
                "xs:double",
                "xs:duration",
                "xs:float",
                "xs:gDay",
                "xs:gMonth",
                "xs:gMonthDay",
                "xs:gYear",
                "xs:gYearMonth",
                "xs:hexBinary",
                "xs:int",
                "xs:integer",
                "xs:long",
                "xs:negativeInteger",
                "xs:nonNegativeInteger",
                "xs:nonPositiveInteger",
                "xs:positiveInteger",
                "xs:short",
                "xs:string",
                "xs:time",
                "xs:unsignedByte",
                "xs:unsignedInt",
                "xs:unsignedLong",
                "xs:unsignedShort"
            ]
        },
        "DataTypeIec61360": {
            "type": "string",
            "enum": [
                "BLOB",
                "BOOLEAN",
                "DATE",
                "FILE",
                "HTML",
                "INTEGER_COUNT",
                "INTEGER_CURRENCY",
                "INTEGER_MEASURE",
                "IRDI",
                "IRI",
                "RATIONAL",
                "RATIONAL_MEASURE",
                "REAL_COUNT",
                "REAL_CURRENCY",
                "REAL_MEASURE",
                "STRING",
                "STRING_TRANSLATABLE",
                "TIME",
                "TIMESTAMP"
            ]
        },
        "EmbeddedDataSpecification": {
            "type": "object",
            "properties": {
                "dataSpecification": {
                    "$ref": "#/definitions/Reference"
                },
                "dataSpecificationContent": {
                    "$ref": "#/definitions/DataSpecificationContent_choice"
                }
            },
            "required": ["dataSpecification", "dataSpecificationContent"]
        },
        "Extension": {
            "allOf": [
                {
                    "$ref": "#/definitions/HasSemantics"
                },
                {
                    "properties": {
                        "name": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 128,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        "valueType": {
                            "$ref": "#/definitions/DataTypeDefXsd"
                        },
                        "value": {
                            "type": "string"
                        },
                        "refersTo": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Reference"
                            },
                            "minItems": 1
                        }
                    },
                    "required": ["name"]
                }
            ]
        },
        "File": {
            "allOf": [
                {
                    "$ref": "#/definitions/DataElement"
                },
                {
                    "properties": {
                        "value": {
                            "type": "string",
                            "allOf": [
                                {
                                    "minLength": 1,
                                    "maxLength": 2000
                                },
                                {
                                    "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                                },
                                {
                                    "pattern": "^file:(//((localhost|(\\[((([0-9A-Fa-f]{1,4}:){6}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::([0-9A-Fa-f]{1,4}:){5}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|([0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){4}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:)?[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){3}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){2}[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){2}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){4}[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(([0-9A-Fa-f]{1,4}:){6}[0-9A-Fa-f]{1,4})?::)|[vV][0-9A-Fa-f]+\\.([a-zA-Z0-9\\-._~]|[!$&'()*+,;=]|:)+)\\]|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])|([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=])*)))?/((([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))+(/(([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))*)*)?|/((([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))+(/(([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))*)*)?)$"
                                }
                            ]
                        },
                        "contentType": {
                            "type": "string",
                            "allOf": [
                                {
                                    "minLength": 1,
                                    "maxLength": 100
                                },
                                {
                                    "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                                },
                                {
                                    "pattern": "^([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+/([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+([ \\t]*;[ \\t]*([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+=(([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+|\"(([\\t !#-\\[\\]-~]|[-ÿ])|\\\\([\\t !-~]|[-ÿ]))*\"))*$"
                                }
                            ]
                        },
                        "modelType": {
                            "const": "File"
                        }
                    },
                    "required": ["contentType"]
                }
            ]
        },
        "HasDataSpecification": {
            "type": "object",
            "properties": {
                "embeddedDataSpecifications": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/EmbeddedDataSpecification"
                    },
                    "minItems": 0
                }
            }
        },
        "HasExtensions": {
            "type": "object",
            "properties": {
                "extensions": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Extension"
                    },
                    "minItems": 1
                }
            }
        },
        "HasKind": {
            "type": "object",
            "properties": {
                "kind": {
                    "$ref": "#/definitions/ModellingKind"
                }
            }
        },
        "HasSemantics": {
            "type": "object",
            "properties": {
                "semanticId": {
                    "$ref": "#/definitions/Reference"
                },
                "supplementalSemanticIds": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Reference"
                    },
                    "minItems": 1
                }
            }
        },
        "Identifiable": {
            "allOf": [
                {
                    "$ref": "#/definitions/Referable"
                },
                {
                    "properties": {
                        "administration": {
                            "$ref": "#/definitions/AdministrativeInformation"
                        },
                        "id": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 2000,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        }
                    },
                    "required": ["id"]
                }
            ]
        },
        "LangStringDefinitionTypeIec61360": {
            "allOf": [
                {
                    "$ref": "#/definitions/AbstractLangString"
                },
                {
                    "properties": {
                        "text": {
                            "maxLength": 1023
                        }
                    }
                }
            ]
        },
        "LangStringNameType": {
            "allOf": [
                {
                    "$ref": "#/definitions/AbstractLangString"
                },
                {
                    "properties": {
                        "text": {
                            "maxLength": 128
                        }
                    }
                }
            ]
        },
        "LangStringPreferredNameTypeIec61360": {
            "allOf": [
                {
                    "$ref": "#/definitions/AbstractLangString"
                },
                {
                    "properties": {
                        "text": {
                            "maxLength": 255
                        }
                    }
                }
            ]
        },
        "LangStringShortNameTypeIec61360": {
            "allOf": [
                {
                    "$ref": "#/definitions/AbstractLangString"
                },
                {
                    "properties": {
                        "text": {
                            "maxLength": 18
                        }
                    }
                }
            ]
        },
        "LangStringTextType": {
            "allOf": [
                {
                    "$ref": "#/definitions/AbstractLangString"
                },
                {
                    "properties": {
                        "text": {
                            "maxLength": 1023
                        }
                    }
                }
            ]
        },
        "LevelType": {
            "type": "object",
            "properties": {
                "min": {
                    "type": "boolean"
                },
                "nom": {
                    "type": "boolean"
                },
                "typ": {
                    "type": "boolean"
                },
                "max": {
                    "type": "boolean"
                }
            },
            "required": ["min", "nom", "typ", "max"]
        },     
        "ModellingKind": {
            "type": "string",
            "enum": ["Instance", "Template"]
        },
        "MultiLanguageProperty": {
            "allOf": [
                {
                    "$ref": "#/definitions/DataElement"
                },
                {
                    "properties": {
                        "value": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/LangStringTextType"
                            },
                            "minItems": 1
                        },
                        "valueId": {
                            "$ref": "#/definitions/Reference"
                        },
                        "modelType": {
                            "const": "MultiLanguageProperty"
                        }
                    }
                }
            ]
        },
        "Property": {
            "allOf": [
                {
                    "$ref": "#/definitions/DataElement"
                },
                {
                    "properties": {
                        "valueType": {
                            "$ref": "#/definitions/DataTypeDefXsd"
                        },
                        "value": {
                            "type": "string"
                        },
                        "valueId": {
                            "$ref": "#/definitions/Reference"
                        },
                        "modelType": {
                            "const": "Property"
                        }
                    },
                    "required": ["valueType"]
                }
            ]
        },
        "Qualifiable": {
            "type": "object",
            "properties": {
                "qualifiers": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Qualifier"
                    },
                    "minItems": 1
                },
                "modelType": {
                    "$ref": "#/definitions/ModelType"
                }
            },
            "required": ["modelType"]
        },
        "Qualifier": {
            "allOf": [
                {
                    "$ref": "#/definitions/HasSemantics"
                },
                {
                    "properties": {
                        "kind": {
                            "$ref": "#/definitions/QualifierKind"
                        },
                        "type": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 128,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        "valueType": {
                            "$ref": "#/definitions/DataTypeDefXsd"
                        },
                        "value": {
                            "type": "string"
                        },
                        "valueId": {
                            "$ref": "#/definitions/Reference"
                        }
                    },
                    "required": ["type", "valueType"]
                }
            ]
        },
        "QualifierKind": {
            "type": "string",
            "enum": ["ConceptQualifier", "TemplateQualifier", "ValueQualifier"]
        },
        "Range": {
            "allOf": [
                {
                    "$ref": "#/definitions/DataElement"
                },
                {
                    "properties": {
                        "valueType": {
                            "$ref": "#/definitions/DataTypeDefXsd"
                        },
                        "min": {
                            "type": "string"
                        },
                        "max": {
                            "type": "string"
                        },
                        "modelType": {
                            "const": "Range"
                        }
                    },
                    "required": ["valueType"]
                }
            ]
        },
        "Referable": {
            "allOf": [
                {
                    "$ref": "#/definitions/HasExtensions"
                },
                {
                    "properties": {
                        "category": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 128,
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        "idShort": {
                            "type": "string",
                            "allOf": [
                                {
                                    "minLength": 1,
                                    "maxLength": 128
                                },
                                {
                                    "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                                },
                                {
                                    "pattern": "^[a-zA-Z][a-zA-Z0-9_]*$"
                                }
                            ]
                        },
                        "displayName": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/LangStringNameType"
                            },
                            "minItems": 1
                        },
                        "description": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/LangStringTextType"
                            },
                            "minItems": 1
                        },
                        "modelType": {
                            "$ref": "#/definitions/ModelType"
                        }
                    },
                    "required": ["modelType"]
                }
            ]
        },
        "Reference": {
            "type": "object",
            "properties": {
                "type": {
                    "$ref": "#/definitions/ReferenceTypes"
                },
                "referredSemanticId": {
                    "$ref": "#/definitions/Reference"
                },
                "keys": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Key"
                    },
                    "minItems": 1
                }
            },
            "required": ["type", "keys"]
        },
        "ReferenceElement": {
            "allOf": [
                {
                    "$ref": "#/definitions/DataElement"
                },
                {
                    "properties": {
                        "value": {
                            "$ref": "#/definitions/Reference"
                        },
                        "modelType": {
                            "const": "ReferenceElement"
                        }
                    }
                }
            ]
        },     
        "Resource": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "allOf": [
                        {
                            "minLength": 1,
                            "maxLength": 2000
                        },
                        {
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        {
                            "pattern": "^file:(//((localhost|(\\[((([0-9A-Fa-f]{1,4}:){6}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|::([0-9A-Fa-f]{1,4}:){5}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|([0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){4}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:)?[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){3}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){2}[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:){2}([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){3}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){4}[0-9A-Fa-f]{1,4})?::([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{1,4}|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9A-Fa-f]{1,4}:){5}[0-9A-Fa-f]{1,4})?::[0-9A-Fa-f]{1,4}|(([0-9A-Fa-f]{1,4}:){6}[0-9A-Fa-f]{1,4})?::)|[vV][0-9A-Fa-f]+\\.([a-zA-Z0-9\\-._~]|[!$&'()*+,;=]|:)+)\\]|([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])|([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=])*)))?/((([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))+(/(([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))*)*)?|/((([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))+(/(([a-zA-Z0-9\\-._~]|%[0-9A-Fa-f][0-9A-Fa-f]|[!$&'()*+,;=]|[:@]))*)*)?)$"
                        }
                    ]
                },
                "contentType": {
                    "type": "string",
                    "allOf": [
                        {
                            "minLength": 1,
                            "maxLength": 100
                        },
                        {
                            "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                        },
                        {
                            "pattern": "^([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+/([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+([ \\t]*;[ \\t]*([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+=(([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+|\"(([\\t !#-\\[\\]-~]|[-ÿ])|\\\\([\\t !-~]|[-ÿ]))*\"))*$"
                        }
                    ]
                }
            },
            "required": ["path"]
        },
        "Submodel": {
            "allOf": [
                {
                    "$ref": "#/definitions/Identifiable"
                },
                {
                    "$ref": "#/definitions/HasKind"
                },
                {
                    "$ref": "#/definitions/HasSemantics"
                },
                {
                    "$ref": "#/definitions/Qualifiable"
                },
                {
                    "$ref": "#/definitions/HasDataSpecification"
                },
                {
                    "properties": {
                        "submodelElements": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/SubmodelElement_choice"
                            },
                            "minItems": 1
                        },
                        "modelType": {
                            "const": "Submodel"
                        }
                    }
                }
            ]
        },
        "SubmodelElement": {
            "allOf": [
                {
                    "$ref": "#/definitions/Referable"
                },
                {
                    "$ref": "#/definitions/HasSemantics"
                },
                {
                    "$ref": "#/definitions/Qualifiable"
                },
                {
                    "$ref": "#/definitions/HasDataSpecification"
                }
            ]
        },
        "SubmodelElementCollection": {
            "allOf": [
                {
                    "$ref": "#/definitions/SubmodelElement"
                },
                {
                    "properties": {
                        "value": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/SubmodelElement_choice"
                            },
                            "minItems": 1
                        },
                        "modelType": {
                            "const": "SubmodelElementCollection"
                        }
                    }
                }
            ]
        },
        "SubmodelElementList": {
            "allOf": [
                {
                    "$ref": "#/definitions/SubmodelElement"
                },
                {
                    "properties": {
                        "orderRelevant": {
                            "type": "boolean"
                        },
                        "semanticIdListElement": {
                            "$ref": "#/definitions/Reference"
                        },
                        "typeValueListElement": {
                            "$ref": "#/definitions/AasSubmodelElements"
                        },
                        "valueTypeListElement": {
                            "$ref": "#/definitions/DataTypeDefXsd"
                        },
                        "value": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/SubmodelElement_choice"
                            },
                            "minItems": 1
                        },
                        "modelType": {
                            "const": "SubmodelElementList"
                        }
                    },
                    "required": ["typeValueListElement"]
                }
            ]
        },
        "SubmodelElement_choice": {
            "oneOf": [
                {
                    "$ref": "#/definitions/File"
                },
                {
                    "$ref": "#/definitions/Property"
                },
                {
                    "$ref": "#/definitions/Range"
                },
                {
                    "$ref": "#/definitions/ReferenceElement"
                },
                {
                    "$ref": "#/definitions/SubmodelElementCollection"
                },
                {
                    "$ref": "#/definitions/SubmodelElementList"
                }
            ]
        },
        "ValueList": {
            "type": "object",
            "properties": {
                "valueReferencePairs": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/ValueReferencePair"
                    },
                    "minItems": 1
                }
            },
            "required": ["valueReferencePairs"]
        },
        "ValueReferencePair": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 2000,
                    "pattern": "^([\\t\\n\\r -퟿-�]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$"
                },
                "valueId": {
                    "$ref": "#/definitions/Reference"
                }
            },
            "required": ["value", "valueId"]
        },
        "value" : {
            "type" : "object",
           
            "properties": {
                "idShort": {
                    "type"  : "string"
                },
                "modelType": {"$ref": "#/definitions/ModelType"}
            },
            "allOf": [
                {
                    "if": {
                        "properties": {
                            "modelType" : {"const": "AssetAdministrationShell"}
                        }
                    },
                    "then": {
                        "properties": {
                            "assetInformation": {"$ref": "#/definitions/AssetInformation"},
                            "submodels" :{
                                "type" : "array",
                                "items": {
                                    "$ref": "#/definitions/element"
                                },
                                "minItems": 0
                            }, 
                            "id" : {"$ref": "#/definitions/UrlType"}
                        }
                    }
                },
                {
                    "if": {
                    "properties": {
                        "modelType" : {"const": "Submodel"}
                            }
                    },
                    "then": {
                        "oneOf" : [
                        {"$ref": "#/definitions/Submodel"}
                        ]
                    }
                }
            ]
            
            
        }
    }
}